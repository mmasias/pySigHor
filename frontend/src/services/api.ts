import axios from 'axios';
import {
  Aula, AulaCreate, AulaUpdate,
  Edificio, EdificioCreate, EdificioUpdate,
  Programa, ProgramaCreate, ProgramaUpdate,
  Curso, CursoCreate, CursoUpdate,
  Profesor, ProfesorCreate, ProfesorUpdate,
  Recurso, RecursoCreate, RecursoUpdate,
  Preferencia, PreferenciaUpdate,
  AsignacionUpdate,
} from '../types';

const API_BASE = '/api/v1';

const apiClient = axios.create({
  baseURL: API_BASE,
  headers: { 'Content-Type': 'application/json' },
});

apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Bearer ${token}`;
  return config;
});

apiClient.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      localStorage.removeItem('user');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// --- Aulas ---
export const aulaService = {
  listarAulas: async (skip = 0, limit = 100): Promise<Aula[]> =>
    (await apiClient.get(`/aulas?skip=${skip}&limit=${limit}`)).data,
  obtenerAula: async (id: number): Promise<Aula> =>
    (await apiClient.get(`/aulas/${id}`)).data,
  crearAula: async (aula: AulaCreate): Promise<Aula> =>
    (await apiClient.post('/aulas', aula)).data,
  actualizarAula: async (id: number, aula: AulaUpdate): Promise<Aula> =>
    (await apiClient.patch(`/aulas/${id}`, aula)).data,
  eliminarAula: async (id: number): Promise<void> =>
    void (await apiClient.delete(`/aulas/${id}`)),
};

// --- Edificios ---
export const edificioService = {
  listarEdificios: async (skip = 0, limit = 100): Promise<Edificio[]> =>
    (await apiClient.get(`/edificios?skip=${skip}&limit=${limit}`)).data,
  obtenerEdificio: async (id: number): Promise<Edificio> =>
    (await apiClient.get(`/edificios/${id}`)).data,
  crearEdificio: async (edificio: EdificioCreate): Promise<Edificio> =>
    (await apiClient.post('/edificios', edificio)).data,
  actualizarEdificio: async (id: number, edificio: EdificioUpdate): Promise<Edificio> =>
    (await apiClient.patch(`/edificios/${id}`, edificio)).data,
  eliminarEdificio: async (id: number): Promise<void> =>
    void (await apiClient.delete(`/edificios/${id}`)),
};

// --- Programas ---
export const programaService = {
  listarProgramas: async (skip = 0, limit = 100): Promise<Programa[]> =>
    (await apiClient.get(`/programas?skip=${skip}&limit=${limit}`)).data,
  obtenerPrograma: async (id: number): Promise<Programa> =>
    (await apiClient.get(`/programas/${id}`)).data,
  crearPrograma: async (programa: ProgramaCreate): Promise<Programa> =>
    (await apiClient.post('/programas', programa)).data,
  actualizarPrograma: async (id: number, programa: ProgramaUpdate): Promise<Programa> =>
    (await apiClient.patch(`/programas/${id}`, programa)).data,
  eliminarPrograma: async (id: number): Promise<void> =>
    void (await apiClient.delete(`/programas/${id}`)),
};

// --- Cursos ---
export const cursoService = {
  listarCursos: async (skip = 0, limit = 100): Promise<Curso[]> =>
    (await apiClient.get(`/cursos?skip=${skip}&limit=${limit}`)).data,
  obtenerCurso: async (id: number): Promise<Curso> =>
    (await apiClient.get(`/cursos/${id}`)).data,
  crearCurso: async (curso: CursoCreate): Promise<Curso> =>
    (await apiClient.post('/cursos', curso)).data,
  actualizarCurso: async (id: number, curso: CursoUpdate): Promise<Curso> =>
    (await apiClient.patch(`/cursos/${id}`, curso)).data,
  eliminarCurso: async (id: number): Promise<void> =>
    void (await apiClient.delete(`/cursos/${id}`)),
};

// --- Profesores ---
export const profesorService = {
  listarProfesores: async (skip = 0, limit = 100): Promise<Profesor[]> =>
    (await apiClient.get(`/profesores?skip=${skip}&limit=${limit}`)).data,
  obtenerProfesor: async (id: number): Promise<Profesor> =>
    (await apiClient.get(`/profesores/${id}`)).data,
  crearProfesor: async (profesor: ProfesorCreate): Promise<Profesor> =>
    (await apiClient.post('/profesores', profesor)).data,
  actualizarProfesor: async (id: number, profesor: ProfesorUpdate): Promise<Profesor> =>
    (await apiClient.patch(`/profesores/${id}`, profesor)).data,
  eliminarProfesor: async (id: number): Promise<void> =>
    void (await apiClient.delete(`/profesores/${id}`)),
};

// --- Recursos ---
export const recursoService = {
  listarRecursos: async (skip = 0, limit = 100): Promise<Recurso[]> =>
    (await apiClient.get(`/recursos?skip=${skip}&limit=${limit}`)).data,
  obtenerRecurso: async (id: number): Promise<Recurso> =>
    (await apiClient.get(`/recursos/${id}`)).data,
  crearRecurso: async (recurso: RecursoCreate): Promise<Recurso> =>
    (await apiClient.post('/recursos', recurso)).data,
  actualizarRecurso: async (id: number, recurso: RecursoUpdate): Promise<Recurso> =>
    (await apiClient.patch(`/recursos/${id}`, recurso)).data,
  eliminarRecurso: async (id: number): Promise<void> =>
    void (await apiClient.delete(`/recursos/${id}`)),
};

// --- Preferencias ---
export const preferenciaService = {
  obtener: async (profesorId: number): Promise<Preferencia[]> =>
    (await apiClient.get(`/profesores/${profesorId}/preferencias`)).data,
  actualizar: async (profesorId: number, data: PreferenciaUpdate): Promise<Preferencia[]> =>
    (await apiClient.put(`/profesores/${profesorId}/preferencias`, data)).data,
};

// --- Asignaciones ---
export const asignacionService = {
  obtener: async (profesorId: number): Promise<Curso[]> =>
    (await apiClient.get(`/profesores/${profesorId}/cursos`)).data,
  actualizar: async (profesorId: number, data: AsignacionUpdate): Promise<Curso[]> =>
    (await apiClient.put(`/profesores/${profesorId}/cursos`, data)).data,
};

// --- Autenticación ---
export const authService = {
  login: async (username: string, password: string): Promise<{ access_token: string; token_type: string }> => {
    const params = new URLSearchParams();
    params.append('username', username);
    params.append('password', password);
    return (await apiClient.post('/auth/login', params, {
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
    })).data;
  },
  verifyToken: async (): Promise<{ username: string }> =>
    (await apiClient.post('/auth/verify-token')).data,
  logout: () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
  },
};
