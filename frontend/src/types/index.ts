// Tipos de dominio
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

// Tipos de autenticación
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
