import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material/styles';
import CssBaseline from '@mui/material/CssBaseline';
import { AuthProvider, useAuth } from './context/AuthContext';
import LoginPage from './pages/LoginPage';
import AulasPage from './pages/AulasPage';
import EdificiosPage from './pages/EdificiosPage';
import ProgramasPage from './pages/ProgramasPage';
import CursosPage from './pages/CursosPage';
import ProfesoresPage from './pages/ProfesoresPage';
import RecursosPage from './pages/RecursosPage';

const theme = createTheme({
  palette: {
    mode: 'light',
  },
});

const ProtectedRoute: React.FC<{ children: React.ReactElement }> = ({ children }) => {
  const { isAuthenticated } = useAuth();
  return isAuthenticated ? children : <Navigate to="/login" />;
};

const App: React.FC = () => {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <AuthProvider>
          <Routes>
            <Route path="/login" element={<LoginPage />} />
            <Route path="/aulas" element={<ProtectedRoute><AulasPage /></ProtectedRoute>} />
            <Route path="/edificios" element={<ProtectedRoute><EdificiosPage /></ProtectedRoute>} />
            <Route path="/programas" element={<ProtectedRoute><ProgramasPage /></ProtectedRoute>} />
            <Route path="/cursos" element={<ProtectedRoute><CursosPage /></ProtectedRoute>} />
            <Route path="/profesores" element={<ProtectedRoute><ProfesoresPage /></ProtectedRoute>} />
            <Route path="/recursos" element={<ProtectedRoute><RecursosPage /></ProtectedRoute>} />
            <Route path="/" element={<Navigate to="/aulas" />} />
          </Routes>
        </AuthProvider>
      </BrowserRouter>
    </ThemeProvider>
  );
};

export default App;
