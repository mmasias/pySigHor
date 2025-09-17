-- =====================================================
-- Script de Creación del Esquema de Base de Datos
-- pySigHor - Sistema Generador de Horarios
-- =====================================================
-- Derivado del Modelo del Dominio RUP
-- Optimizado para algoritmo de 4 fases de optimización
-- =====================================================

-- Extensiones necesarias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- =====================================================
-- TABLAS PRINCIPALES (Entidades del Dominio RUP)
-- =====================================================

-- Tabla: programas
-- Derivada de: Entidad "Programa" del modelo del dominio
CREATE TABLE programas (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: edificios  
-- Derivada de: Entidad "Edificio" del modelo del dominio
CREATE TABLE edificios (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: recursos
-- Derivada de: Entidad "Recurso" del modelo del dominio  
CREATE TABLE recursos (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: profesores
-- Derivada de: Entidad "Profesor" del modelo del dominio
-- Incluye campos de autenticación para caso de uso iniciarSesion()
CREATE TABLE profesores (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nombres VARCHAR(255) NOT NULL,
    apellidos VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE,
    telefono VARCHAR(20),
    activo BOOLEAN DEFAULT TRUE,
    -- Campos de autenticación
    username VARCHAR(50) UNIQUE,
    password_hash VARCHAR(255),
    ultimo_login TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Tabla: aulas
-- Derivada de: Entidad "Aula" del modelo del dominio
-- Relación: Aula pertenece a Edificio
CREATE TABLE aulas (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    capacidad INTEGER NOT NULL CHECK (capacidad > 0),
    edificio_id INTEGER NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (edificio_id) REFERENCES edificios(id)
);

-- Tabla: cursos
-- Derivada de: Entidad "Curso" del modelo del dominio
-- Relación: Curso pertenece a Programa
CREATE TABLE cursos (
    id SERIAL PRIMARY KEY,
    codigo VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(255) NOT NULL,
    descripcion TEXT,
    creditos INTEGER NOT NULL CHECK (creditos > 0),
    horas_teoricas INTEGER DEFAULT 0,
    horas_practicas INTEGER DEFAULT 0,
    vacantes INTEGER NOT NULL CHECK (vacantes > 0),
    bloque_horario VARCHAR(5) NOT NULL,
    programa_id INTEGER NOT NULL,
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (programa_id) REFERENCES programas(id),
    CONSTRAINT chk_bloque_horario CHECK (bloque_horario IN ('H1','H2','H3','H4','H5','H6','H7','H8','HE','HV'))
);

-- =====================================================
-- TABLA INTEGRADORA (Resultado del Algoritmo)
-- =====================================================

-- Tabla: horarios
-- Derivada de: Entidad "Horario" del modelo del dominio
-- Propósito: Materializar la solución del algoritmo de optimización
-- Agregación: Horario referencia Profesor, Curso y Aula
CREATE TABLE horarios (
    id SERIAL PRIMARY KEY,
    -- Referencias a entidades del dominio (agregación del análisis RUP)
    profesor_id INTEGER NOT NULL,
    curso_id INTEGER NOT NULL,
    aula_id INTEGER NOT NULL,
    -- Datos temporales del horario asignado
    bloque_horario VARCHAR(5) NOT NULL,
    dias_semana VARCHAR(10) NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fin TIME NOT NULL,
    -- Metadatos del algoritmo de generación
    algoritmo_version VARCHAR(10) DEFAULT '1.0',
    puntuacion_compatibilidad DECIMAL(5,2),
    fecha_generacion TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    generado_por INTEGER,
    -- Constraints de integridad derivadas del dominio
    FOREIGN KEY (profesor_id) REFERENCES profesores(id),
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    FOREIGN KEY (aula_id) REFERENCES aulas(id),
    FOREIGN KEY (generado_por) REFERENCES profesores(id),
    -- Validaciones de dominio
    CONSTRAINT chk_horario_bloque CHECK (bloque_horario IN ('H1','H2','H3','H4','H5','H6','H7','H8','HE','HV')),
    CONSTRAINT chk_dias_semana CHECK (dias_semana ~ '^[LMXJVS]+$'),
    CONSTRAINT chk_horas CHECK (hora_fin > hora_inicio),
    -- Prevención de conflictos (un profesor/aula no puede estar en dos lugares a la vez)
    UNIQUE (profesor_id, bloque_horario, dias_semana, hora_inicio),
    UNIQUE (aula_id, bloque_horario, dias_semana, hora_inicio)
);

-- =====================================================
-- TABLAS DE RELACIÓN (Many-to-Many)
-- =====================================================

-- Tabla: profesor_recursos
-- Propósito: Preferencias de profesores sobre recursos específicos
-- Utilizada por: Algoritmo GeneraPreHorario() para optimización dual
CREATE TABLE profesor_recursos (
    profesor_id INTEGER,
    recurso_id INTEGER,
    nivel_preferencia INTEGER DEFAULT 3 CHECK (nivel_preferencia BETWEEN 1 AND 5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (profesor_id, recurso_id),
    FOREIGN KEY (profesor_id) REFERENCES profesores(id) ON DELETE CASCADE,
    FOREIGN KEY (recurso_id) REFERENCES recursos(id) ON DELETE CASCADE
);

-- Tabla: aula_recursos  
-- Propósito: Recursos disponibles en cada aula
-- Utilizada por: Algoritmo GeneraPreHorario() para matching aula-profesor
CREATE TABLE aula_recursos (
    aula_id INTEGER,
    recurso_id INTEGER,
    cantidad INTEGER DEFAULT 1 CHECK (cantidad > 0),
    estado VARCHAR(20) DEFAULT 'disponible',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (aula_id, recurso_id),
    FOREIGN KEY (aula_id) REFERENCES aulas(id) ON DELETE CASCADE,
    FOREIGN KEY (recurso_id) REFERENCES recursos(id) ON DELETE CASCADE,
    CONSTRAINT chk_estado CHECK (estado IN ('disponible', 'mantenimiento', 'fuera_servicio'))
);

-- =====================================================
-- TABLAS TEMPORALES (Algoritmo de Optimización)
-- =====================================================

-- Tabla: temp_cursos_h_modificado
-- Propósito: Almacenar resultados de PrepararH() - Fase 1 del algoritmo
-- Temporalidad: Se limpia después de cada generación de horarios
CREATE TABLE temp_cursos_h_modificado (
    curso_id INTEGER,
    bloque_original VARCHAR(5),
    bloque_asignado VARCHAR(5) NOT NULL,
    motivo_cambio VARCHAR(50),
    fase_algoritmo INTEGER DEFAULT 1,
    session_id UUID NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (curso_id) REFERENCES cursos(id),
    PRIMARY KEY (curso_id, session_id)
);

-- Tabla: temp_aula_ocupada
-- Propósito: Control de ocupación durante GeneraPreHorario() - Fase 2
-- Temporalidad: Se limpia después de cada generación de horarios  
CREATE TABLE temp_aula_ocupada (
    aula_id INTEGER,
    bloque_horario VARCHAR(5),
    session_id UUID,
    curso_asignado_id INTEGER,
    reservado_hasta TIMESTAMP,
    PRIMARY KEY (aula_id, bloque_horario, session_id),
    FOREIGN KEY (aula_id) REFERENCES aulas(id),
    FOREIGN KEY (curso_asignado_id) REFERENCES cursos(id)
);

-- =====================================================
-- ÍNDICES DE OPTIMIZACIÓN PARA EL ALGORITMO
-- =====================================================

-- Índices para PrepararH() - Resolución de conflictos
CREATE INDEX idx_cursos_bloque_programa ON cursos(bloque_horario, programa_id);
CREATE INDEX idx_cursos_vacantes_desc ON cursos(vacantes DESC);
CREATE INDEX idx_temp_cursos_session ON temp_cursos_h_modificado(session_id, bloque_asignado);

-- Índices para GeneraPreHorario() - Optimización dual
CREATE INDEX idx_aulas_capacidad_edificio ON aulas(capacidad, edificio_id);
CREATE INDEX idx_profesor_recursos_nivel ON profesor_recursos(profesor_id, nivel_preferencia DESC);
CREATE INDEX idx_aula_recursos_cantidad ON aula_recursos(aula_id, cantidad) WHERE estado = 'disponible';
CREATE INDEX idx_temp_aula_session ON temp_aula_ocupada(session_id, bloque_horario);

-- Índices para consultas de horarios (consultarHorario)
CREATE INDEX idx_horarios_profesor_bloque ON horarios(profesor_id, bloque_horario);
CREATE INDEX idx_horarios_aula_fecha ON horarios(aula_id, fecha_generacion);
CREATE INDEX idx_horarios_curso ON horarios(curso_id);
CREATE INDEX idx_horarios_fecha_generacion ON horarios(fecha_generacion DESC);

-- Índices para casos de uso CRUD
CREATE INDEX idx_programas_activo ON programas(activo) WHERE activo = TRUE;
CREATE INDEX idx_cursos_programa_activo ON cursos(programa_id, activo) WHERE activo = TRUE;
CREATE INDEX idx_profesores_username ON profesores(username) WHERE activo = TRUE;
CREATE INDEX idx_aulas_edificio_activo ON aulas(edificio_id, activo) WHERE activo = TRUE;

-- =====================================================
-- FUNCIONES DE UTILIDAD
-- =====================================================

-- Función: generar_session_id
-- Propósito: Generar UUID único para cada sesión de algoritmo
CREATE OR REPLACE FUNCTION generar_session_id()
RETURNS UUID AS $$
BEGIN
    RETURN uuid_generate_v4();
END;
$$ LANGUAGE plpgsql;

-- Función: limpiar_tablas_temporales  
-- Propósito: Limpiar datos temporales después de generación de horarios
CREATE OR REPLACE FUNCTION limpiar_tablas_temporales(p_session_id UUID)
RETURNS VOID AS $$
BEGIN
    DELETE FROM temp_cursos_h_modificado WHERE session_id = p_session_id;
    DELETE FROM temp_aula_ocupada WHERE session_id = p_session_id;
END;
$$ LANGUAGE plpgsql;

-- Función: calcular_compatibilidad_aula_profesor
-- Propósito: Calcular puntuación de compatibilidad para optimización dual
CREATE OR REPLACE FUNCTION calcular_compatibilidad_aula_profesor(
    p_profesor_id INTEGER,
    p_aula_id INTEGER
)
RETURNS DECIMAL(5,2) AS $$
DECLARE
    v_puntuacion DECIMAL(5,2) := 0.0;
    v_recursos_coincidentes INTEGER := 0;
    v_total_preferencias INTEGER := 0;
BEGIN
    -- Contar preferencias del profesor
    SELECT COUNT(*) INTO v_total_preferencias
    FROM profesor_recursos 
    WHERE profesor_id = p_profesor_id;
    
    -- Si no tiene preferencias, puntuación neutra
    IF v_total_preferencias = 0 THEN
        RETURN 50.0;
    END IF;
    
    -- Contar recursos coincidentes entre preferencias del profesor y aula
    SELECT COUNT(*) INTO v_recursos_coincidentes
    FROM profesor_recursos pr
    INNER JOIN aula_recursos ar ON pr.recurso_id = ar.recurso_id
    WHERE pr.profesor_id = p_profesor_id 
      AND ar.aula_id = p_aula_id
      AND ar.estado = 'disponible';
    
    -- Calcular puntuación: (coincidencias / total_preferencias) * 100
    v_puntuacion := (v_recursos_coincidentes::DECIMAL / v_total_preferencias::DECIMAL) * 100;
    
    RETURN v_puntuacion;
END;
$$ LANGUAGE plpgsql;

-- =====================================================
-- TRIGGERS PARA AUDITORÍA
-- =====================================================

-- Función para actualizar timestamp de updated_at
CREATE OR REPLACE FUNCTION actualizar_updated_at()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Aplicar trigger a tablas principales
CREATE TRIGGER trg_programas_updated_at BEFORE UPDATE ON programas FOR EACH ROW EXECUTE FUNCTION actualizar_updated_at();
CREATE TRIGGER trg_cursos_updated_at BEFORE UPDATE ON cursos FOR EACH ROW EXECUTE FUNCTION actualizar_updated_at();
CREATE TRIGGER trg_profesores_updated_at BEFORE UPDATE ON profesores FOR EACH ROW EXECUTE FUNCTION actualizar_updated_at();
CREATE TRIGGER trg_aulas_updated_at BEFORE UPDATE ON aulas FOR EACH ROW EXECUTE FUNCTION actualizar_updated_at();
CREATE TRIGGER trg_edificios_updated_at BEFORE UPDATE ON edificios FOR EACH ROW EXECUTE FUNCTION actualizar_updated_at();
CREATE TRIGGER trg_recursos_updated_at BEFORE UPDATE ON recursos FOR EACH ROW EXECUTE FUNCTION actualizar_updated_at();
CREATE TRIGGER trg_aula_recursos_updated_at BEFORE UPDATE ON aula_recursos FOR EACH ROW EXECUTE FUNCTION actualizar_updated_at();

-- =====================================================
-- COMENTARIOS EN TABLAS (Documentación)
-- =====================================================

COMMENT ON TABLE programas IS 'Programas académicos (carreras universitarias)';
COMMENT ON TABLE cursos IS 'Cursos/materias que se dictan en los programas';
COMMENT ON TABLE profesores IS 'Docentes que imparten cursos - incluye autenticación';
COMMENT ON TABLE aulas IS 'Espacios físicos donde se realizan las clases';
COMMENT ON TABLE edificios IS 'Edificios del campus que contienen aulas';
COMMENT ON TABLE recursos IS 'Recursos/equipamiento disponible (proyector, laboratorio, etc.)';
COMMENT ON TABLE horarios IS 'Tabla integradora - resultado del algoritmo de optimización';
COMMENT ON TABLE profesor_recursos IS 'Preferencias de profesores sobre recursos específicos';
COMMENT ON TABLE aula_recursos IS 'Recursos disponibles en cada aula';
COMMENT ON TABLE temp_cursos_h_modificado IS 'Temporal - resultados de PrepararH() (Fase 1)';
COMMENT ON TABLE temp_aula_ocupada IS 'Temporal - control ocupación GeneraPreHorario() (Fase 2)';

-- =====================================================
-- PERMISOS Y SEGURIDAD
-- =====================================================

-- Crear rol para aplicación
CREATE ROLE pysighor_app WITH LOGIN ENCRYPTED PASSWORD 'change_me_in_production';

-- Permisos sobre tablas principales
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO pysighor_app;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO pysighor_app;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO pysighor_app;

-- Crear rol de solo lectura para consultas
CREATE ROLE pysighor_readonly WITH LOGIN ENCRYPTED PASSWORD 'readonly_password';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO pysighor_readonly;

-- =====================================================
-- SCRIPT COMPLETADO
-- =====================================================
-- Este script crea la estructura completa de la base de datos
-- derivada del análisis RUP completado de pySigHor
-- Optimizada para el algoritmo de generación de horarios de 4 fases
-- =====================================================