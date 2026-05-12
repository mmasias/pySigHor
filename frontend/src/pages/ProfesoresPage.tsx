import React, { useState, useEffect } from 'react';
import {
  Box, Button, Container, Typography, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, IconButton, Dialog, DialogTitle,
  DialogContent, DialogActions, TextField, Alert,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import { useAuth } from '../context/AuthContext';
import { profesorService } from '../services/api';
import { Profesor, ProfesorCreate } from '../types';

const ProfesoresPage: React.FC = () => {
  const { user, logout } = useAuth();
  const [profesores, setProfesores] = useState<Profesor[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [editingProfesor, setEditingProfesor] = useState<Profesor | null>(null);
  const [formData, setFormData] = useState<ProfesorCreate>({ nombres: '', apellidos: '' });

  const cargarProfesores = async () => {
    setLoading(true);
    setError('');
    try {
      setProfesores(await profesorService.listarProfesores());
    } catch {
      setError('Error al cargar profesores');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { cargarProfesores(); }, []);

  const handleOpenCreate = () => {
    setEditingProfesor(null);
    setFormData({ nombres: '', apellidos: '', correo: '', telefono: '', observaciones: '' });
    setOpenDialog(true);
  };

  const handleOpenEdit = (profesor: Profesor) => {
    setEditingProfesor(profesor);
    setFormData({
      nombres: profesor.nombres,
      apellidos: profesor.apellidos,
      correo: profesor.correo || '',
      telefono: profesor.telefono || '',
      observaciones: profesor.observaciones || '',
    });
    setOpenDialog(true);
  };

  const handleCloseDialog = () => { setOpenDialog(false); setEditingProfesor(null); setError(''); };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      if (editingProfesor) {
        const updated = await profesorService.actualizarProfesor(editingProfesor.id, formData);
        setProfesores(profesores.map((p) => (p.id === updated.id ? updated : p)));
      } else {
        const created = await profesorService.crearProfesor(formData);
        setProfesores([...profesores, created]);
      }
      handleCloseDialog();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al guardar profesor');
    }
  };

  const handleDelete = async (profesor: Profesor) => {
    if (!window.confirm(`¿Eliminar al profesor "${profesor.nombres} ${profesor.apellidos}"?`)) return;
    try {
      await profesorService.eliminarProfesor(profesor.id);
      setProfesores(profesores.filter((p) => p.id !== profesor.id));
    } catch {
      setError('Error al eliminar profesor');
    }
  };

  if (!user) return <Container><Typography variant="h6">Cargando...</Typography></Container>;

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography component="h1" variant="h4" gutterBottom>Gestión de Profesores</Typography>
        <Box>
          <Button color="inherit" onClick={logout} sx={{ mr: 2 }}>Logout</Button>
          <Button variant="contained" startIcon={<AddIcon />} onClick={handleOpenCreate}>Nuevo Profesor</Button>
        </Box>
      </Box>

      {error && <Alert severity="error" sx={{ my: 2 }} onClose={() => setError('')}>{error}</Alert>}

      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nombres</TableCell>
              <TableCell>Apellidos</TableCell>
              <TableCell>Correo</TableCell>
              <TableCell>Teléfono</TableCell>
              <TableCell>Acciones</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {loading ? (
              <TableRow><TableCell colSpan={6} align="center">Cargando...</TableCell></TableRow>
            ) : profesores.length === 0 ? (
              <TableRow><TableCell colSpan={6} align="center">No hay profesores registrados</TableCell></TableRow>
            ) : (
              profesores.map((profesor) => (
                <TableRow key={profesor.id}>
                  <TableCell>{profesor.id}</TableCell>
                  <TableCell>{profesor.nombres}</TableCell>
                  <TableCell>{profesor.apellidos}</TableCell>
                  <TableCell>{profesor.correo || '-'}</TableCell>
                  <TableCell>{profesor.telefono || '-'}</TableCell>
                  <TableCell>
                    <IconButton onClick={() => handleOpenEdit(profesor)} size="small"><EditIcon /></IconButton>
                    <IconButton onClick={() => handleDelete(profesor)} size="small" color="error"><DeleteIcon /></IconButton>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={openDialog} onClose={handleCloseDialog} maxWidth="sm" fullWidth>
        <DialogTitle>{editingProfesor ? 'Editar Profesor' : 'Nuevo Profesor'}</DialogTitle>
        <DialogContent>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
            <TextField margin="normal" required fullWidth label="Nombres"
              value={formData.nombres}
              onChange={(e) => setFormData({ ...formData, nombres: e.target.value })} />
            <TextField margin="normal" required fullWidth label="Apellidos"
              value={formData.apellidos}
              onChange={(e) => setFormData({ ...formData, apellidos: e.target.value })} />
            <TextField margin="normal" fullWidth label="Correo electrónico" type="email"
              value={formData.correo || ''}
              onChange={(e) => setFormData({ ...formData, correo: e.target.value })} />
            <TextField margin="normal" fullWidth label="Teléfono"
              value={formData.telefono || ''}
              onChange={(e) => setFormData({ ...formData, telefono: e.target.value })} />
            <TextField margin="normal" fullWidth multiline rows={3} label="Observaciones"
              value={formData.observaciones || ''}
              onChange={(e) => setFormData({ ...formData, observaciones: e.target.value })} />
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancelar</Button>
          <Button onClick={handleSubmit} variant="contained">{editingProfesor ? 'Actualizar' : 'Crear'}</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default ProfesoresPage;
