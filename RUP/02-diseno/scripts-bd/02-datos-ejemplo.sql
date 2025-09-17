-- =====================================================
-- Datos de Ejemplo para Testing - pySigHor
-- =====================================================
-- Propósito: Datos mínimos para validar casos de uso RUP
-- Base: Sistema original SigHor de la Universidad de Piura
-- =====================================================

-- =====================================================
-- DATOS MAESTROS
-- =====================================================

-- Programas académicos
INSERT INTO programas (codigo, nombre, descripcion) VALUES
('PI', 'Ingeniería de Sistemas e Informática', 'Programa de pregrado en ingeniería de sistemas'),
('PC', 'Ciencias de la Computación', 'Programa de pregrado en ciencias de la computación'),
('PS', 'Ingeniería de Software', 'Programa de especialización en ingeniería de software'),
('PE', 'Ingeniería Electrónica', 'Programa de pregrado en ingeniería electrónica');

-- Recursos disponibles
INSERT INTO recursos (codigo, nombre, descripcion) VALUES
('PROJ', 'Proyector', 'Proyector multimedia para presentaciones'),
('LAB', 'Laboratorio', 'Laboratorio de cómputo con PCs'),
('WIFI', 'WiFi', 'Conexión inalámbrica de alta velocidad'),
('AC', 'Aire Acondicionado', 'Sistema de climatización'),
('AUDIO', 'Sistema de Audio', 'Amplificación y micrófono'),
('PIZARRA', 'Pizarra Digital', 'Pizarra interactiva digital');

-- Edificios del campus
INSERT INTO edificios (codigo, nombre, descripcion) VALUES
('A', 'Edificio A - Aulas', 'Edificio principal de aulas de pregrado'),
('B', 'Edificio B - Laboratorios', 'Edificio de laboratorios de ingeniería'),
('C', 'Edificio C - Posgrado', 'Edificio dedicado a programas de posgrado'),
('D', 'Edificio D - Biblioteca', 'Edificio de biblioteca con aulas de estudio');

-- Aulas por edificio
INSERT INTO aulas (codigo, nombre, capacidad, edificio_id) VALUES
-- Edificio A - Aulas estándar
('A101', 'Aula A101', 40, 1),
('A102', 'Aula A102', 45, 1),
('A103', 'Aula A103', 35, 1),
('A201', 'Aula A201', 50, 1),
('A202', 'Aula A202', 40, 1),
-- Edificio B - Laboratorios
('B101', 'Lab Sistemas 1', 30, 2),
('B102', 'Lab Sistemas 2', 25, 2),
('B201', 'Lab Electrónica', 20, 2),
-- Edificio C - Aulas especializadas
('C101', 'Aula Magna', 100, 3),
('C102', 'Sala de Conferencias', 60, 3),
-- Edificio D - Aulas pequeñas
('D101', 'Aula Seminario 1', 15, 4),
('D102', 'Aula Seminario 2', 20, 4);

-- Profesores (incluye datos de autenticación para testing)
INSERT INTO profesores (codigo, nombres, apellidos, email, username, password_hash, activo) VALUES
('P001', 'Juan Carlos', 'García Mendoza', 'jgarcia@udep.pe', 'jgarcia', '$2a$10$rZ8qQ9XoP5.5LxYyK9CqKO4K5YjYxB6jJ8T2fF3dT7gQ9B2pN5sK.', TRUE),
('P002', 'María Elena', 'Rodríguez Silva', 'mrodriguez@udep.pe', 'mrodriguez', '$2a$10$sA9rR0YpQ6.6MyZzL0DrLP5L6ZkZyC7kK9U3gG4eU8hR0C3qO6tL.', TRUE),
('P003', 'Carlos Alberto', 'Fernández López', 'cfernandez@udep.pe', 'cfernandez', '$2a$10$tB0sS1ZqR7.7NzA0M1EsMP6M7AlAzD8lL0V4hH5fV9iS1D4rP7uM.', TRUE),
('P004', 'Ana Patricia', 'Vásquez Torres', 'avasquez@udep.pe', 'avasquez', '$2a$10$uC1tT2ArS8.8OzB1N2FtNQ7N8BmBzE9mM1W5iI6gW0jT2E5sQ8vN.', TRUE),
('P005', 'Luis Miguel', 'Herrera Castro', 'lherrera@udep.pe', 'lherrera', '$2a$10$vD2uU3BsT9.9PzC2O3GuOQ8O9CnCzF0nN2X6jJ7hX1kU3F6tR9wO.', TRUE);

-- Cursos por programa con bloque horario asignado
INSERT INTO cursos (codigo, nombre, descripcion, creditos, horas_teoricas, horas_practicas, vacantes, bloque_horario, programa_id) VALUES
-- Programa PI (Ingeniería de Sistemas)
('PI101', 'Introducción a la Programación', 'Fundamentos de programación en Python', 4, 3, 2, 40, 'H1', 1),
('PI102', 'Estructura de Datos', 'Listas, pilas, colas y árboles', 4, 3, 2, 35, 'H2', 1),
('PI201', 'Base de Datos', 'Diseño y administración de bases de datos', 4, 2, 4, 30, 'H3', 1),
('PI202', 'Ingeniería de Software', 'Metodologías de desarrollo de software', 3, 3, 0, 35, 'H4', 1),
-- Programa PC (Ciencias de la Computación)  
('PC101', 'Matemática Discreta', 'Lógica, teoría de conjuntos y grafos', 3, 3, 0, 25, 'H1', 2),
('PC102', 'Algoritmos y Complejidad', 'Análisis de algoritmos y complejidad', 4, 3, 2, 30, 'H2', 2),
('PC201', 'Inteligencia Artificial', 'Machine Learning y redes neuronales', 4, 2, 4, 25, 'H5', 2),
-- Programa PS (Ingeniería de Software)
('PS101', 'Arquitectura de Software', 'Patrones y estilos arquitectónicos', 3, 2, 2, 20, 'H3', 3),
('PS102', 'Testing y Calidad', 'Pruebas de software y aseguramiento de calidad', 3, 2, 2, 20, 'H6', 3),
-- Programa PE (Ingeniería Electrónica)
('PE101', 'Circuitos Digitales', 'Diseño de circuitos lógicos', 4, 2, 4, 25, 'H4', 4),
('PE102', 'Microcontroladores', 'Programación de sistemas embebidos', 4, 2, 4, 20, 'H7', 4);

-- =====================================================
-- RELACIONES Y PREFERENCIAS
-- =====================================================

-- Recursos disponibles en cada aula
INSERT INTO aula_recursos (aula_id, recurso_id, cantidad, estado) VALUES
-- Edificio A - Aulas estándar con proyector básico
(1, 1, 1, 'disponible'), -- A101: Proyector
(1, 3, 1, 'disponible'), -- A101: WiFi
(2, 1, 1, 'disponible'), -- A102: Proyector  
(2, 3, 1, 'disponible'), -- A102: WiFi
(2, 4, 1, 'disponible'), -- A102: AC
(3, 1, 1, 'disponible'), -- A103: Proyector
(3, 3, 1, 'disponible'), -- A103: WiFi
(4, 1, 1, 'disponible'), -- A201: Proyector
(4, 3, 1, 'disponible'), -- A201: WiFi
(4, 4, 1, 'disponible'), -- A201: AC
(4, 5, 1, 'disponible'), -- A201: Audio
(5, 1, 1, 'disponible'), -- A202: Proyector
(5, 3, 1, 'disponible'), -- A202: WiFi
-- Edificio B - Laboratorios completamente equipados
(6, 1, 1, 'disponible'), -- B101: Proyector
(6, 2, 30, 'disponible'), -- B101: 30 PCs
(6, 3, 1, 'disponible'), -- B101: WiFi
(6, 4, 1, 'disponible'), -- B101: AC
(7, 1, 1, 'disponible'), -- B102: Proyector
(7, 2, 25, 'disponible'), -- B102: 25 PCs
(7, 3, 1, 'disponible'), -- B102: WiFi
(7, 4, 1, 'disponible'), -- B102: AC
(8, 1, 1, 'disponible'), -- B201: Proyector (Lab Electrónica)
(8, 3, 1, 'disponible'), -- B201: WiFi
(8, 4, 1, 'disponible'), -- B201: AC
-- Edificio C - Aulas premium
(9, 1, 2, 'disponible'), -- C101: 2 Proyectores
(9, 3, 1, 'disponible'), -- C101: WiFi
(9, 4, 1, 'disponible'), -- C101: AC
(9, 5, 1, 'disponible'), -- C101: Audio
(9, 6, 1, 'disponible'), -- C101: Pizarra Digital
(10, 1, 1, 'disponible'), -- C102: Proyector
(10, 3, 1, 'disponible'), -- C102: WiFi
(10, 4, 1, 'disponible'), -- C102: AC
(10, 5, 1, 'disponible'), -- C102: Audio
-- Edificio D - Aulas básicas
(11, 3, 1, 'disponible'), -- D101: Solo WiFi
(12, 1, 1, 'disponible'), -- D102: Proyector
(12, 3, 1, 'disponible'); -- D102: WiFi

-- Preferencias de profesores sobre recursos
INSERT INTO profesor_recursos (profesor_id, recurso_id, nivel_preferencia) VALUES
-- Juan Carlos García (P001) - Prefiere laboratorios y proyector
(1, 1, 5), -- Proyector (máxima preferencia)
(1, 2, 5), -- Laboratorio (máxima preferencia)
(1, 3, 4), -- WiFi (alta preferencia)
(1, 4, 3), -- AC (preferencia media)
-- María Elena Rodríguez (P002) - Prefiere presentaciones multimedia
(2, 1, 5), -- Proyector
(2, 5, 4), -- Audio
(2, 6, 4), -- Pizarra Digital
(2, 4, 4), -- AC
(2, 3, 3), -- WiFi
-- Carlos Alberto Fernández (P003) - Especialista en laboratorios
(3, 2, 5), -- Laboratorio (máxima preferencia)
(3, 1, 4), -- Proyector
(3, 3, 5), -- WiFi (conexión crítica)
(3, 4, 2), -- AC (baja preferencia)
-- Ana Patricia Vásquez (P004) - Aulas tradicionales
(4, 1, 4), -- Proyector
(4, 6, 3), -- Pizarra Digital
(4, 4, 4), -- AC (importante para comodidad)
(4, 3, 3), -- WiFi
-- Luis Miguel Herrera (P005) - Flexible, sin preferencias fuertes
(5, 1, 3), -- Proyector
(5, 3, 3), -- WiFi
(5, 4, 2); -- AC

-- =====================================================
-- DATOS DE EJEMPLO PARA ALGORITMO
-- =====================================================

-- Ejemplo de horario generado (para testing de consultarHorario)
-- Representa una solución parcial del algoritmo
INSERT INTO horarios (profesor_id, curso_id, aula_id, bloque_horario, dias_semana, hora_inicio, hora_fin, puntuacion_compatibilidad, generado_por) VALUES
-- H1: Lunes, Miércoles, Viernes 07:00-08:00
(1, 1, 6, 'H1', 'LXV', '07:00', '08:00', 100.0, 1), -- Juan García - PI101 en Lab B101
(3, 5, 1, 'H1', 'LXV', '07:00', '08:00', 60.0, 1),  -- Carlos Fernández - PC101 en A101
-- H2: Martes, Jueves, Sábado 07:00-08:00  
(1, 2, 7, 'H2', 'MJS', '07:00', '08:00', 100.0, 1), -- Juan García - PI102 en Lab B102
(3, 6, 2, 'H2', 'MJS', '07:00', '08:00', 60.0, 1),  -- Carlos Fernández - PC102 en A102
-- H3: Lunes, Miércoles, Viernes 09:00-10:00
(2, 3, 6, 'H3', 'LXV', '09:00', '10:00', 85.0, 1),  -- María Rodríguez - PI201 en Lab B101
(4, 8, 4, 'H3', 'LXV', '09:00', '10:00', 75.0, 1),  -- Ana Vásquez - PS101 en A201
-- H4: Martes, Jueves, Sábado 09:00-10:00
(2, 4, 4, 'H4', 'MJS', '09:00', '10:00', 70.0, 1),  -- María Rodríguez - PI202 en A201
(5, 10, 8, 'H4', 'MJS', '09:00', '10:00', 65.0, 1); -- Luis Herrera - PE101 en B201

-- =====================================================
-- DATOS PARA TESTING DE CASOS DE USO
-- =====================================================

-- Usuario administrador para testing del login
-- Password: "admin123" (hasheado con BCrypt)
UPDATE profesores 
SET username = 'admin', 
    password_hash = '$2a$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi',
    activo = TRUE
WHERE codigo = 'P001';

-- Comentarios para documentación
COMMENT ON TABLE profesor_recursos IS 'Nivel 1=mínimo, 5=máximo. Usado por algoritmo GeneraPreHorario()';
COMMENT ON TABLE aula_recursos IS 'Estado: disponible|mantenimiento|fuera_servicio';
COMMENT ON TABLE horarios IS 'puntuacion_compatibilidad: resultado de optimización dual (0-100)';

-- Estadísticas para validación
SELECT 'Datos cargados correctamente:' as mensaje;
SELECT 'Programas: ' || COUNT(*) FROM programas;
SELECT 'Cursos: ' || COUNT(*) FROM cursos;
SELECT 'Profesores: ' || COUNT(*) FROM profesores;
SELECT 'Aulas: ' || COUNT(*) FROM aulas;
SELECT 'Recursos: ' || COUNT(*) FROM recursos;
SELECT 'Preferencias: ' || COUNT(*) FROM profesor_recursos;
SELECT 'Horarios ejemplo: ' || COUNT(*) FROM horarios;

-- =====================================================
-- VALIDACIONES DE INTEGRIDAD
-- =====================================================

-- Verificar que todos los cursos tienen programa asignado
SELECT 'Cursos sin programa:' as validacion, COUNT(*) as cantidad
FROM cursos c LEFT JOIN programas p ON c.programa_id = p.id
WHERE p.id IS NULL;

-- Verificar que todas las aulas tienen edificio asignado  
SELECT 'Aulas sin edificio:' as validacion, COUNT(*) as cantidad
FROM aulas a LEFT JOIN edificios e ON a.edificio_id = e.id
WHERE e.id IS NULL;

-- Verificar que todos los horarios tienen referencias válidas
SELECT 'Horarios con referencias inválidas:' as validacion, COUNT(*) as cantidad
FROM horarios h
LEFT JOIN profesores p ON h.profesor_id = p.id
LEFT JOIN cursos c ON h.curso_id = c.id  
LEFT JOIN aulas a ON h.aula_id = a.id
WHERE p.id IS NULL OR c.id IS NULL OR a.id IS NULL;

-- =====================================================
-- SCRIPT DE DATOS COMPLETADO
-- =====================================================
-- Datos mínimos para validar todos los casos de uso RUP:
-- - iniciarSesion(): usuario admin/admin123
-- - CRUD completo: programas, cursos, profesores, aulas, etc.
-- - generarHorario(): datos suficientes para algoritmo
-- - consultarHorario(): horarios de ejemplo pre-generados
-- =====================================================