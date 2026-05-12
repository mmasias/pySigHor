// --- Aula ---
export interface Aula {
  id: number;
  nombre: string;
  capacidad: number;
  especial: boolean;
  bloqueada: boolean;
  id_edificio: number | null;
}
export interface AulaCreate {
  nombre: string;
  capacidad: number;
  especial?: boolean;
  bloqueada?: boolean;
  id_edificio?: number;
}
export interface AulaUpdate {
  nombre?: string;
  capacidad?: number;
  especial?: boolean;
  bloqueada?: boolean;
  id_edificio?: number;
}

// --- Edificio ---
export interface Edificio {
  id: number;
  nombre: string;
  direccion: string | null;
}
export interface EdificioCreate {
  nombre: string;
  direccion?: string;
}
export interface EdificioUpdate {
  nombre?: string;
  direccion?: string;
}

// --- Programa ---
export interface Programa {
  id: number;
  nombre: string;
  descripcion: string | null;
  activo: boolean;
}
export interface ProgramaCreate {
  nombre: string;
  descripcion?: string;
  activo?: boolean;
}
export interface ProgramaUpdate {
  nombre?: string;
  descripcion?: string;
  activo?: boolean;
}

// --- Curso ---
export interface Curso {
  id: number;
  nombre: string;
  descripcion: string | null;
  creditos: number | null;
  horas: number | null;
  id_programa: number | null;
}
export interface CursoCreate {
  nombre: string;
  descripcion?: string;
  creditos?: number;
  horas?: number;
  id_programa?: number;
}
export interface CursoUpdate {
  nombre?: string;
  descripcion?: string;
  creditos?: number;
  horas?: number;
  id_programa?: number;
}

// --- Profesor ---
export interface Profesor {
  id: number;
  nombres: string;
  apellidos: string;
  correo: string | null;
  telefono: string | null;
  observaciones: string | null;
}
export interface ProfesorCreate {
  nombres: string;
  apellidos: string;
  correo?: string;
  telefono?: string;
  observaciones?: string;
}
export interface ProfesorUpdate {
  nombres?: string;
  apellidos?: string;
  correo?: string;
  telefono?: string;
  observaciones?: string;
}

// --- Recurso ---
export interface Recurso {
  id: number;
  nombre: string;
  descripcion: string | null;
}
export interface RecursoCreate {
  nombre: string;
  descripcion?: string;
}
export interface RecursoUpdate {
  nombre?: string;
  descripcion?: string;
}

// --- Autenticación ---
export interface LoginRequest {
  username: string;
  password: string;
}
export interface TokenResponse {
  access_token: string;
  token_type: string;
}
export interface AuthUser {
  username: string;
  token: string;
}
