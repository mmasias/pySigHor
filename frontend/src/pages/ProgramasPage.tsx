import React, { useState, useEffect } from 'react';
import {
  Box, Button, Container, Typography, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, IconButton, Dialog, DialogTitle,
  DialogContent, DialogActions, TextField, Switch, Alert,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import { useAuth } from '../context/AuthContext';
import { programaService } from '../services/api';
import { Programa, ProgramaCreate } from '../types';

const ProgramasPage: React.FC = () => {
  const { user, logout } = useAuth();
  const [programas, setProgramas] = useState<Programa[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [editingPrograma, setEditingPrograma] = useState<Programa | null>(null);
  const [formData, setFormData] = useState<ProgramaCreate>({ nombre: '', descripcion: '', activo: true });

  const cargarProgramas = async () => {
    setLoading(true);
    setError('');
    try {
      setProgramas(await programaService.listarProgramas());
    } catch {
      setError('Error al cargar programas');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { cargarProgramas(); }, []);

  const handleOpenCreate = () => {
    setEditingPrograma(null);
    setFormData({ nombre: '', descripcion: '', activo: true });
    setOpenDialog(true);
  };

  const handleOpenEdit = (programa: Programa) => {
    setEditingPrograma(programa);
    setFormData({ nombre: programa.nombre, descripcion: programa.descripcion || '', activo: programa.activo });
    setOpenDialog(true);
  };

  const handleCloseDialog = () => { setOpenDialog(false); setEditingPrograma(null); setError(''); };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      if (editingPrograma) {
        const updated = await programaService.actualizarPrograma(editingPrograma.id, formData);
        setProgramas(programas.map((p) => (p.id === updated.id ? updated : p)));
      } else {
        const created = await programaService.crearPrograma(formData);
        setProgramas([...programas, created]);
      }
      handleCloseDialog();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al guardar programa');
    }
  };

  const handleDelete = async (programa: Programa) => {
    if (!window.confirm(`¿Eliminar el programa "${programa.nombre}"?`)) return;
    try {
      await programaService.eliminarPrograma(programa.id);
      setProgramas(programas.filter((p) => p.id !== programa.id));
    } catch {
      setError('Error al eliminar programa');
    }
  };

  if (!user) return <Container><Typography variant="h6">Cargando...</Typography></Container>;

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography component="h1" variant="h4" gutterBottom>Gestión de Programas</Typography>
        <Box>
          <Button color="inherit" onClick={logout} sx={{ mr: 2 }}>Logout</Button>
          <Button variant="contained" startIcon={<AddIcon />} onClick={handleOpenCreate}>Nuevo Programa</Button>
        </Box>
      </Box>

      {error && <Alert severity="error" sx={{ my: 2 }} onClose={() => setError('')}>{error}</Alert>}

      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nombre</TableCell>
              <TableCell>Descripción</TableCell>
              <TableCell>Activo</TableCell>
              <TableCell>Acciones</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {loading ? (
              <TableRow><TableCell colSpan={5} align="center">Cargando...</TableCell></TableRow>
            ) : programas.length === 0 ? (
              <TableRow><TableCell colSpan={5} align="center">No hay programas registrados</TableCell></TableRow>
            ) : (
              programas.map((programa) => (
                <TableRow key={programa.id}>
                  <TableCell>{programa.id}</TableCell>
                  <TableCell>{programa.nombre}</TableCell>
                  <TableCell>{programa.descripcion || '-'}</TableCell>
                  <TableCell>{programa.activo ? 'Sí' : 'No'}</TableCell>
                  <TableCell>
                    <IconButton onClick={() => handleOpenEdit(programa)} size="small"><EditIcon /></IconButton>
                    <IconButton onClick={() => handleDelete(programa)} size="small" color="error"><DeleteIcon /></IconButton>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={openDialog} onClose={handleCloseDialog} maxWidth="sm" fullWidth>
        <DialogTitle>{editingPrograma ? 'Editar Programa' : 'Nuevo Programa'}</DialogTitle>
        <DialogContent>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
            <TextField margin="normal" required fullWidth label="Nombre"
              value={formData.nombre}
              onChange={(e) => setFormData({ ...formData, nombre: e.target.value })} />
            <TextField margin="normal" fullWidth multiline rows={2} label="Descripción"
              value={formData.descripcion || ''}
              onChange={(e) => setFormData({ ...formData, descripcion: e.target.value })} />
            <Box sx={{ display: 'flex', alignItems: 'center', mt: 2 }}>
              <Switch checked={formData.activo ?? true}
                onChange={(e) => setFormData({ ...formData, activo: e.target.checked })} />
              <Typography sx={{ ml: 1 }}>Activo</Typography>
            </Box>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancelar</Button>
          <Button onClick={handleSubmit} variant="contained">{editingPrograma ? 'Actualizar' : 'Crear'}</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default ProgramasPage;
