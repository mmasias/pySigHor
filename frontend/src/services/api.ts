import axios from 'axios';
import { Aula, AulaCreate, AulaUpdate } from '../types';

const API_BASE = '/api/v1';

// Cliente axios configurado
const apiClient = axios.create({
  baseURL: API_BASE,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor para agregar token
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Servicio de Aulas
export const aulaService = {
  // Listar todas las aulas
  listarAulas: async (skip = 0, limit = 100): Promise<Aula[]> => {
    const response = await apiClient.get(`/aulas?skip=${skip}&limit=${limit}`);
    return response.data;
  },

  // Obtener un aula por ID
  obtenerAula: async (id: number): Promise<Aula> => {
    const response = await apiClient.get(`/aulas/${id}`);
    return response.data;
  },

  // Crear nueva aula
  crearAula: async (aula: AulaCreate): Promise<Aula> => {
    const response = await apiClient.post('/aulas', aula);
    return response.data;
  },

  // Actualizar aula existente
  actualizarAula: async (id: number, aula: AulaUpdate): Promise<Aula> => {
    const response = await apiClient.patch(`/aulas/${id}`, aula);
    return response.data;
  },

  // Eliminar aula
  eliminarAula: async (id: number): Promise<void> => {
    await apiClient.delete(`/aulas/${id}`);
  },
};

// Servicio de Autenticación
export const authService = {
  login: async (username: string, password: string): Promise<{ access_token: string; token_type: string }> => {
    // OAuth2PasswordRequestForm requiere application/x-www-form-urlencoded
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);

    const response = await apiClient.post('/auth/login', params, {
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
    });
    return response.data;
  },

  verifyToken: async (): Promise<{ username: string }> => {
    const response = await apiClient.post('/auth/verify-token');
    return response.data;
  },

  logout: () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  },
};
