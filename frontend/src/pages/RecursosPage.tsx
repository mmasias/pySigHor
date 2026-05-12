import React, { useState, useEffect } from 'react';
import {
  Box, Button, Container, Typography, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, IconButton, Dialog, DialogTitle,
  DialogContent, DialogActions, TextField, Alert,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import { useAuth } from '../context/AuthContext';
import { recursoService } from '../services/api';
import { Recurso, RecursoCreate } from '../types';

const RecursosPage: React.FC = () => {
  const { user, logout } = useAuth();
  const [recursos, setRecursos] = useState<Recurso[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [editingRecurso, setEditingRecurso] = useState<Recurso | null>(null);
  const [formData, setFormData] = useState<RecursoCreate>({ nombre: '', descripcion: '' });

  const cargarRecursos = async () => {
    setLoading(true);
    setError('');
    try {
      setRecursos(await recursoService.listarRecursos());
    } catch {
      setError('Error al cargar recursos');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { cargarRecursos(); }, []);

  const handleOpenCreate = () => {
    setEditingRecurso(null);
    setFormData({ nombre: '', descripcion: '' });
    setOpenDialog(true);
  };

  const handleOpenEdit = (recurso: Recurso) => {
    setEditingRecurso(recurso);
    setFormData({ nombre: recurso.nombre, descripcion: recurso.descripcion || '' });
    setOpenDialog(true);
  };

  const handleCloseDialog = () => { setOpenDialog(false); setEditingRecurso(null); setError(''); };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      if (editingRecurso) {
        const updated = await recursoService.actualizarRecurso(editingRecurso.id, formData);
        setRecursos(recursos.map((r) => (r.id === updated.id ? updated : r)));
      } else {
        const created = await recursoService.crearRecurso(formData);
        setRecursos([...recursos, created]);
      }
      handleCloseDialog();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al guardar recurso');
    }
  };

  const handleDelete = async (recurso: Recurso) => {
    if (!window.confirm(`¿Eliminar el recurso "${recurso.nombre}"?`)) return;
    try {
      await recursoService.eliminarRecurso(recurso.id);
      setRecursos(recursos.filter((r) => r.id !== recurso.id));
    } catch {
      setError('Error al eliminar recurso');
    }
  };

  if (!user) return <Container><Typography variant="h6">Cargando...</Typography></Container>;

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography component="h1" variant="h4" gutterBottom>Gestión de Recursos</Typography>
        <Box>
          <Button color="inherit" onClick={logout} sx={{ mr: 2 }}>Logout</Button>
          <Button variant="contained" startIcon={<AddIcon />} onClick={handleOpenCreate}>Nuevo Recurso</Button>
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
              <TableCell>Acciones</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {loading ? (
              <TableRow><TableCell colSpan={4} align="center">Cargando...</TableCell></TableRow>
            ) : recursos.length === 0 ? (
              <TableRow><TableCell colSpan={4} align="center">No hay recursos registrados</TableCell></TableRow>
            ) : (
              recursos.map((recurso) => (
                <TableRow key={recurso.id}>
                  <TableCell>{recurso.id}</TableCell>
                  <TableCell>{recurso.nombre}</TableCell>
                  <TableCell>{recurso.descripcion || '-'}</TableCell>
                  <TableCell>
                    <IconButton onClick={() => handleOpenEdit(recurso)} size="small"><EditIcon /></IconButton>
                    <IconButton onClick={() => handleDelete(recurso)} size="small" color="error"><DeleteIcon /></IconButton>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={openDialog} onClose={handleCloseDialog} maxWidth="sm" fullWidth>
        <DialogTitle>{editingRecurso ? 'Editar Recurso' : 'Nuevo Recurso'}</DialogTitle>
        <DialogContent>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
            <TextField margin="normal" required fullWidth label="Nombre"
              value={formData.nombre}
              onChange={(e) => setFormData({ ...formData, nombre: e.target.value })} />
            <TextField margin="normal" fullWidth multiline rows={2} label="Descripción"
              value={formData.descripcion || ''}
              onChange={(e) => setFormData({ ...formData, descripcion: e.target.value })} />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancelar</Button>
          <Button onClick={handleSubmit} variant="contained">{editingRecurso ? 'Actualizar' : 'Crear'}</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default RecursosPage;
