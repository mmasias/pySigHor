import React, { useState, useEffect } from 'react';
import {
  Box, Button, Container, Typography, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, IconButton, Dialog, DialogTitle,
  DialogContent, DialogActions, TextField, Alert,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import { useAuth } from '../context/AuthContext';
import { edificioService } from '../services/api';
import { Edificio, EdificioCreate } from '../types';

const EdificiosPage: React.FC = () => {
  const { user, logout } = useAuth();
  const [edificios, setEdificios] = useState<Edificio[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [editingEdificio, setEditingEdificio] = useState<Edificio | null>(null);
  const [formData, setFormData] = useState<EdificioCreate>({ nombre: '', direccion: '' });

  const cargarEdificios = async () => {
    setLoading(true);
    setError('');
    try {
      setEdificios(await edificioService.listarEdificios());
    } catch {
      setError('Error al cargar edificios');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { cargarEdificios(); }, []);

  const handleOpenCreate = () => {
    setEditingEdificio(null);
    setFormData({ nombre: '', direccion: '' });
    setOpenDialog(true);
  };

  const handleOpenEdit = (edificio: Edificio) => {
    setEditingEdificio(edificio);
    setFormData({ nombre: edificio.nombre, direccion: edificio.direccion || '' });
    setOpenDialog(true);
  };

  const handleCloseDialog = () => { setOpenDialog(false); setEditingEdificio(null); setError(''); };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      if (editingEdificio) {
        const updated = await edificioService.actualizarEdificio(editingEdificio.id, formData);
        setEdificios(edificios.map((e) => (e.id === updated.id ? updated : e)));
      } else {
        const created = await edificioService.crearEdificio(formData);
        setEdificios([...edificios, created]);
      }
      handleCloseDialog();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al guardar edificio');
    }
  };

  const handleDelete = async (edificio: Edificio) => {
    if (!window.confirm(`¿Eliminar el edificio "${edificio.nombre}"?`)) return;
    try {
      await edificioService.eliminarEdificio(edificio.id);
      setEdificios(edificios.filter((e) => e.id !== edificio.id));
    } catch {
      setError('Error al eliminar edificio');
    }
  };

  if (!user) return <Container><Typography variant="h6">Cargando...</Typography></Container>;

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography component="h1" variant="h4" gutterBottom>Gestión de Edificios</Typography>
        <Box>
          <Button color="inherit" onClick={logout} sx={{ mr: 2 }}>Logout</Button>
          <Button variant="contained" startIcon={<AddIcon />} onClick={handleOpenCreate}>Nuevo Edificio</Button>
        </Box>
      </Box>

      {error && <Alert severity="error" sx={{ my: 2 }} onClose={() => setError('')}>{error}</Alert>}

      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nombre</TableCell>
              <TableCell>Dirección</TableCell>
              <TableCell>Acciones</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {loading ? (
              <TableRow><TableCell colSpan={4} align="center">Cargando...</TableCell></TableRow>
            ) : edificios.length === 0 ? (
              <TableRow><TableCell colSpan={4} align="center">No hay edificios registrados</TableCell></TableRow>
            ) : (
              edificios.map((edificio) => (
                <TableRow key={edificio.id}>
                  <TableCell>{edificio.id}</TableCell>
                  <TableCell>{edificio.nombre}</TableCell>
                  <TableCell>{edificio.direccion || '-'}</TableCell>
                  <TableCell>
                    <IconButton onClick={() => handleOpenEdit(edificio)} size="small"><EditIcon /></IconButton>
                    <IconButton onClick={() => handleDelete(edificio)} size="small" color="error"><DeleteIcon /></IconButton>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={openDialog} onClose={handleCloseDialog} maxWidth="sm" fullWidth>
        <DialogTitle>{editingEdificio ? 'Editar Edificio' : 'Nuevo Edificio'}</DialogTitle>
        <DialogContent>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
            <TextField margin="normal" required fullWidth label="Nombre"
              value={formData.nombre}
              onChange={(e) => setFormData({ ...formData, nombre: e.target.value })} />
            <TextField margin="normal" fullWidth label="Dirección"
              value={formData.direccion || ''}
              onChange={(e) => setFormData({ ...formData, direccion: e.target.value })} />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancelar</Button>
          <Button onClick={handleSubmit} variant="contained">{editingEdificio ? 'Actualizar' : 'Crear'}</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default EdificiosPage;
