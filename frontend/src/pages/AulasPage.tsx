import React, { useState, useEffect } from 'react';
import {
  Box,
  Button,
  Container,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  TextField,
  Switch,
  Alert,
  FormControl,
  InputLabel,
  Select,
  SelectChangeEvent,
  MenuItem,
  Checkbox,
  ListItemText,
  OutlinedInput,
} from '@mui/material';
import {
  Edit as EditIcon,
  Delete as DeleteIcon,
  Add as AddIcon,
} from '@mui/icons-material';
import { useAuth } from '../context/AuthContext';
import { aulaService, edificioService, recursoService } from '../services/api';
import { Aula, AulaCreate, AulaUpdate, Edificio, Recurso } from '../types';

const AulasPage: React.FC = () => {
  const { user, logout } = useAuth();
  const [aulas, setAulas] = useState<Aula[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [openDialog, setOpenDialog] = useState(false);
  const [editingAula, setEditingAula] = useState<Aula | null>(null);
  const [formData, setFormData] = useState<AulaCreate>({
    nombre: '',
    capacidad: 0,
    especial: false,
    bloqueada: false,
  });
  const [edificios, setEdificios] = useState<Edificio[]>([]);
  const [recursos, setRecursos] = useState<Recurso[]>([]);
  const [selectedRecursos, setSelectedRecursos] = useState<number[]>([]);

  const cargarAulas = async () => {
    setLoading(true);
    setError('');
    try {
      const data = await aulaService.listarAulas();
      setAulas(data);
    } catch (err: any) {
      setError('Error al cargar aulas');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    cargarAulas();
  }, []);

  useEffect(() => { edificioService.listarEdificios().then(setEdificios); }, []);
  useEffect(() => { recursoService.listarRecursos().then(setRecursos); }, []);

  const handleOpenCreate = () => {
    setEditingAula(null);
    setFormData({
      nombre: '',
      capacidad: 0,
      especial: false,
      bloqueada: false,
    });
    setSelectedRecursos([]);
    setOpenDialog(true);
  };

  const handleOpenEdit = (aula: Aula) => {
    setEditingAula(aula);
    setFormData({
      nombre: aula.nombre,
      capacidad: aula.capacidad,
      especial: aula.especial,
      bloqueada: aula.bloqueada,
      id_edificio: aula.id_edificio || undefined,
    });
    setSelectedRecursos(aula.recursos.map((r) => r.id));
    setOpenDialog(true);
  };

  const handleCloseDialog = () => {
    setOpenDialog(false);
    setEditingAula(null);
    setError('');
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    try {
      if (editingAula) {
        const updateData: AulaUpdate = { ...formData, ids_recursos: selectedRecursos };
        const updated = await aulaService.actualizarAula(editingAula.id, updateData);
        setAulas(aulas.map((a) => (a.id === updated.id ? updated : a)));
      } else {
        const created = await aulaService.crearAula(formData);
        setAulas([...aulas, created]);
      }
      handleCloseDialog();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Error al guardar aula');
    }
  };

  const handleDelete = async (aula: Aula) => {
    if (!window.confirm(`¿Eliminar el aula "${aula.nombre}"?`)) {
      return;
    }

    try {
      await aulaService.eliminarAula(aula.id);
      setAulas(aulas.filter((a) => a.id !== aula.id));
    } catch (err: any) {
      setError('Error al eliminar aula');
    }
  };

  if (!user) {
    return (
      <Container>
        <Typography variant="h6">Cargando...</Typography>
      </Container>
    );
  }

  return (
    <Container maxWidth="lg">
      <Box sx={{ mt: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Typography component="h1" variant="h4" gutterBottom>
          Gestión de Aulas
        </Typography>
        <Box>
          <Button color="inherit" onClick={logout} sx={{ mr: 2 }}>
            Logout
          </Button>
          <Button variant="contained" startIcon={<AddIcon />} onClick={handleOpenCreate}>
            Nueva Aula
          </Button>
        </Box>
      </Box>

      {error && (
        <Alert severity="error" sx={{ my: 2 }} onClose={() => setError('')}>
          {error}
        </Alert>
      )}

      <TableContainer>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>ID</TableCell>
              <TableCell>Nombre</TableCell>
              <TableCell>Capacidad</TableCell>
              <TableCell>Edificio</TableCell>
              <TableCell>Recursos</TableCell>
              <TableCell>Especial</TableCell>
              <TableCell>Bloqueada</TableCell>
              <TableCell>Acciones</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {loading ? (
              <TableRow>
                <TableCell colSpan={8} align="center">
                  Cargando...
                </TableCell>
              </TableRow>
            ) : aulas.length === 0 ? (
              <TableRow>
                <TableCell colSpan={8} align="center">
                  No hay aulas registradas
                </TableCell>
              </TableRow>
            ) : (
              aulas.map((aula) => (
                <TableRow key={aula.id}>
                  <TableCell>{aula.id}</TableCell>
                  <TableCell>{aula.nombre}</TableCell>
                  <TableCell>{aula.capacidad}</TableCell>
                  <TableCell>{edificios.find((e) => e.id === aula.id_edificio)?.nombre ?? '-'}</TableCell>
                  <TableCell>{aula.recursos.length > 0 ? aula.recursos.map((r) => r.nombre).join(', ') : '-'}</TableCell>
                  <TableCell>{aula.especial ? 'Sí' : 'No'}</TableCell>
                  <TableCell>{aula.bloqueada ? 'Sí' : 'No'}</TableCell>
                  <TableCell>
                    <IconButton onClick={() => handleOpenEdit(aula)} size="small">
                      <EditIcon />
                    </IconButton>
                    <IconButton onClick={() => handleDelete(aula)} size="small" color="error">
                      <DeleteIcon />
                    </IconButton>
                  </TableCell>
                </TableRow>
              ))
            )}
          </TableBody>
        </Table>
      </TableContainer>

      <Dialog open={openDialog} onClose={handleCloseDialog} maxWidth="sm" fullWidth>
        <DialogTitle>{editingAula ? 'Editar Aula' : 'Nueva Aula'}</DialogTitle>
        <DialogContent>
          <Box component="form" onSubmit={handleSubmit} sx={{ mt: 2 }}>
            <TextField
              margin="normal"
              required
              fullWidth
              label="Nombre"
              value={formData.nombre}
              onChange={(e) => setFormData({ ...formData, nombre: e.target.value })}
            />
            <TextField
              margin="normal"
              required
              fullWidth
              type="number"
              label="Capacidad"
              value={formData.capacidad}
              onChange={(e) => setFormData({ ...formData, capacidad: parseInt(e.target.value) })}
              inputProps={{ min: 0, max: 255 }}
            />
            <FormControl fullWidth margin="normal">
              <InputLabel id="edificio-label">Edificio</InputLabel>
              <Select
                labelId="edificio-label"
                label="Edificio"
                value={formData.id_edificio ?? ''}
                onChange={(e: SelectChangeEvent<number | ''>) =>
                  setFormData({ ...formData, id_edificio: e.target.value === '' ? undefined : Number(e.target.value) })
                }
              >
                <MenuItem value=""><em>Sin edificio</em></MenuItem>
                {edificios.map((ed) => (
                  <MenuItem key={ed.id} value={ed.id}>{ed.nombre}</MenuItem>
                ))}
              </Select>
            </FormControl>
            <FormControl fullWidth margin="normal">
              <InputLabel id="recursos-label">Recursos</InputLabel>
              <Select
                labelId="recursos-label"
                multiple
                value={selectedRecursos}
                onChange={(e: SelectChangeEvent<number[]>) => {
                  setSelectedRecursos(e.target.value as number[]);
                }}
                input={<OutlinedInput label="Recursos" />}
                renderValue={(selected) =>
                  recursos
                    .filter((r) => (selected as number[]).includes(r.id))
                    .map((r) => r.nombre)
                    .join(', ')
                }
              >
                {recursos.map((rec) => (
                  <MenuItem key={rec.id} value={rec.id}>
                    <Checkbox checked={selectedRecursos.includes(rec.id)} />
                    <ListItemText primary={rec.nombre} />
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
              <Switch
                checked={formData.especial}
                onChange={(e) => setFormData({ ...formData, especial: e.target.checked })}
              />
              <Typography sx={{ ml: 1 }}>Especial</Typography>
            </Box>
            <Box sx={{ display: 'flex', alignItems: 'center', mt: 2 }}>
              <Switch
                checked={formData.bloqueada}
                onChange={(e) => setFormData({ ...formData, bloqueada: e.target.checked })}
              />
              <Typography sx={{ ml: 1 }}>Bloqueada</Typography>
            </Box>
          </Box>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleCloseDialog}>Cancelar</Button>
          <Button onClick={handleSubmit} variant="contained">
            {editingAula ? 'Actualizar' : 'Crear'}
          </Button>
        </DialogActions>
      </Dialog>
    </Container>
  );
};

export default AulasPage;
