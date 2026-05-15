import React, { useState, useEffect } from 'react';
import {
  Box, Button, Container, Typography, Table, TableBody, TableCell,
  TableContainer, TableHead, TableRow, IconButton, Dialog, DialogTitle,
  DialogContent, DialogActions, TextField, Alert,
  FormControl, InputLabel, Select, SelectChangeEvent, MenuItem,
} from '@mui/material';
import { Edit as EditIcon, Delete as DeleteIcon, Add as AddIcon } from '@mui/icons-material';
import { useAuth } from '../context/AuthContext';
import { cursoService, programaService } from '../services/api';
import { Curso, CursoCreate, Programa } from '../types';

const CursosPage: React.FC = () => {
  const { user, logout } = useAuth();
  const [cursos, setCursos] = useState<Curso[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [editingCurso, setEditingCurso] = useState<Curso | null>(null);
  const [formData, setFormData] = useState<CursoCreate>({ nombre: '' });
  const [programas, setProgramas] = useState<Programa[]>([]);

  const cargarCursos = async () => {
    setLoading(true);
    setError('');
    try {
      setCursos(await cursoService.listarCursos());
    } catch {
      setError('Error al cargar cursos');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { cargarCursos(); }, []);
  useEffect(() => { programaService.listarProgramas().then(setProgramas); }, []);

  const handleOpenCreate = () => {
    setEditingCurso(null);
    setFormData({ nombre: '', descripcion: '', creditos: undefined, horas: undefined });
    setOpenDialog(true);
  };

  const handleOpenEdit = (curso: Curso) => {
    setEditingCurso(curso);
    setFormData({
      nombre: curso.nombre,
      descripcion: curso.descripcion || '',
      creditos: curso.creditos ?? undefined,
      horas: curso.horas ?? undefined,
      id_programa: curso.id_programa ?? undefined,
    });
    setOpenDialog(true);
  };

  const handleCloseDialog = () => { setOpenDialog(false); setEditingCurso(null); setError(''); };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    try {
      if (editingCurso) {
        const updated = await cursoService.actualizarCurso(editingCurso.id, formData);
        setCursos(cursos.map((c) => (c.id === updated.id ? updated : c)));
      } else {
        const created = await cursoService.crearCurso(formData);
        setCursos([...cursos, created]);
      }
      handleCloseDialog();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al guardar curso');
    }
  };

  const handleDelete = async (curso: Curso) => {
    if (!window.confirm(`¿Eliminar el curso "${curso.nombre}"?`)) return;
    try {
      await cursoService.eliminarCurso(curso.id);
      setCursos(cursos.filter((c) => c.id !== curso.id));
    } catch {
      setError('Error al eliminar curso');
    }
  };

  if (!user) return <Container><Typography variant="h6">Cargando...</Typography></Container>;

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography component="h1" variant="h4" gutterBottom>Gestión de Cursos</Typography>
        <Box>
          <Button color="inherit" onClick={logout} sx={{ mr: 2 }}>Logout</Button>
          <Button variant="contained" startIcon={<AddIcon />} onClick={handleOpenCreate}>Nuevo Curso</Button>
        </Box>
      </Box>

      {error && <Alert severity="error" sx={{ my: 2 }} onClose={() => setError('')}>{error}</Alert>}

      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nombre</TableCell>
              <TableCell>Créditos</TableCell>
              <TableCell>Horas</TableCell>
              <TableCell>Acciones</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {loading ? (
              <TableRow><TableCell colSpan={5} align="center">Cargando...</TableCell></TableRow>
            ) : cursos.length === 0 ? (
              <TableRow><TableCell colSpan={5} align="center">No hay cursos registrados</TableCell></TableRow>
            ) : (
              cursos.map((curso) => (
                <TableRow key={curso.id}>
                  <TableCell>{curso.id}</TableCell>
                  <TableCell>{curso.nombre}</TableCell>
                  <TableCell>{curso.creditos ?? '-'}</TableCell>
                  <TableCell>{curso.horas ?? '-'}</TableCell>
                  <TableCell>
                    <IconButton onClick={() => handleOpenEdit(curso)} size="small"><EditIcon /></IconButton>
                    <IconButton onClick={() => handleDelete(curso)} size="small" color="error"><DeleteIcon /></IconButton>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={openDialog} onClose={handleCloseDialog} maxWidth="sm" fullWidth>
        <DialogTitle>{editingCurso ? 'Editar Curso' : 'Nuevo Curso'}</DialogTitle>
        <DialogContent>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
            <TextField margin="normal" required fullWidth label="Nombre"
              value={formData.nombre}
              onChange={(e) => setFormData({ ...formData, nombre: e.target.value })} />
            <TextField margin="normal" fullWidth multiline rows={2} label="Descripción"
              value={formData.descripcion || ''}
              onChange={(e) => setFormData({ ...formData, descripcion: e.target.value })} />
            <TextField margin="normal" fullWidth type="number" label="Créditos"
              value={formData.creditos ?? ''}
              onChange={(e) => setFormData({ ...formData, creditos: e.target.value ? parseInt(e.target.value) : undefined })}
              inputProps={{ min: 0 }} />
            <TextField margin="normal" fullWidth type="number" label="Horas semanales"
              value={formData.horas ?? ''}
              onChange={(e) => setFormData({ ...formData, horas: e.target.value ? parseInt(e.target.value) : undefined })}
              inputProps={{ min: 0 }} />
            <FormControl fullWidth margin="normal">
              <InputLabel id="programa-label">Programa</InputLabel>
              <Select
                labelId="programa-label"
                label="Programa"
                value={formData.id_programa ?? ''}
                onChange={(e: SelectChangeEvent<number | ''>) =>
                  setFormData({ ...formData, id_programa: e.target.value === '' ? undefined : Number(e.target.value) })
                }
              >
                <MenuItem value=""><em>Sin programa</em></MenuItem>
                {programas.map((prog) => (
                  <MenuItem key={prog.id} value={prog.id}>{prog.nombre}</MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancelar</Button>
          <Button onClick={handleSubmit} variant="contained">{editingCurso ? 'Actualizar' : 'Crear'}</Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default CursosPage;
