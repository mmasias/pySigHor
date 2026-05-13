import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { authService } from '../services/api';
import { AuthUser } from '../types';

interface AuthContextType {
  user: AuthUser | null;
  login: (username: string, password: string) => Promise<void>;
  logout: () => void;
  isAuthenticated: boolean;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider = ({ children }: { children: ReactNode }) => {
  const [user, setUser] = useState<AuthUser | null>(null);

  // Verificar si hay token almacenado al cargar
  useEffect(() => {
    const verifyStoredToken = async () => {
      const token = localStorage.getItem('token');
      const username = localStorage.getItem('user');
      if (token && username) {
        try {
          await authService.verifyToken();
          setUser({ username, token });
        } catch {
          localStorage.removeItem('token');
          localStorage.removeItem('user');
        }
      }
    };
    verifyStoredToken();
  }, []);

  const login = async (username: string, password: string) => {
    try {
      const response = await authService.login(username, password);
      const authUser: AuthUser = {
        username,
        token: response.access_token,
      };

      localStorage.setItem('token', response.access_token);
      localStorage.setItem('user', username);
      setUser(authUser);
    } catch (error) {
      console.error('Error en login:', error);
      throw error;
    }
  };

  const logout = () => {
    authService.logout();
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        login,
        logout,
        isAuthenticated: !!user,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth debe usarse dentro de AuthProvider');
  }
  return context;
};
