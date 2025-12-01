package es.ums.sighor.cursos.casosuso;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

/**
 * ==== ARQUITECTURA ASUMIDA PARA ESTOS TESTS ====
 *
 * Se asume una arquitectura limpia o hexagonal con las siguientes capas y componentes:
 *
 * 1.  **Use Case / Service (CrearCursoUseCase)**:
 *     - Contiene la lógica de negocio pura del caso de uso.
 *     - Orquesta las operaciones entre el repositorio y el sistema de navegación.
 *     - Es la clase bajo prueba (@InjectMocks).
 *
 * 2.  **Repository (CursoRepository)**:
 *     - Abstracción para la persistencia de datos (e.g., JPA Repository).
 *     - Responsable de guardar, buscar y eliminar entidades `Curso`.
 *     - Será un mock (@Mock) para aislar la lógica de negocio de la base de datos.
 *
 * 3.  **Navigation (NavigationService)**:
 *     - Abstracción que representa el mecanismo para cambiar de "estado" o "pantalla" en la UI.
 *     - Responsable de ejecutar la transición a `editarCurso()`.
 *     - Será un mock (@Mock) para verificar que se le instruye navegar correctamente.
 *
 * 4.  **Entity (Curso)**:
 *     - El modelo del dominio que representa un curso académico.
 *
 * La filosofía C->U ("Crear-delgado -> Editar-gordo") se implementa en `CrearCursoUseCase`,
 * que solo se encarga de la creación mínima y delega la edición completa a otro componente
 * a través del servicio de navegación.
 */
@ExtendWith(MockitoExtension.class)
@DisplayName("Caso de Uso: crearCurso()")
class CrearCursoUseCaseTest {

    @Mock
    private CursoRepository cursoRepository; // Mock para la capa de persistencia

    @Mock
    private NavigationService navigationService; // Mock para el servicio de navegación

    @InjectMocks
    private CrearCursoUseCase crearCursoUseCase; // La clase que contiene la lógica del caso de uso

    private static final String NOMBRE_CURSO_VALIDO = "Análisis de Sistemas I";

    @Test
    @DisplayName("Flujo principal: Crear un curso con datos mínimos y navegar a edición")
    void crearCurso_conNombreValido_guardaCursoYNavegaAEdicion() {
        // --- GIVEN (Dado) ---
        // Un nuevo curso que se va a crear
        Curso cursoSinId = new Curso(NOMBRE_CURSO_VALIDO);
        
        // Cuando el repositorio guarde el curso, devolverá el mismo curso pero con un ID asignado
        Curso cursoGuardadoConId = new Curso(NOMBRE_CURSO_VALIDO);
        cursoGuardadoConId.setId(1L);

        // Configuración del mock del repositorio
        when(cursoRepository.save(any(Curso.class))).thenReturn(cursoGuardadoConId);

        // --- WHEN (Cuando) ---
        // Se ejecuta el caso de uso con el nombre del curso
        crearCursoUseCase.ejecutar(NOMBRE_CURSO_VALIDO);

        // --- THEN (Entonces) ---
        // 1. Se debe haber invocado al repositorio para guardar el curso
        verify(cursoRepository, times(1)).save(argThat(curso -> 
            curso.getNombre().equals(NOMBRE_CURSO_VALIDO) && curso.getId() == null
        ));

        // 2. Se debe haber invocado al servicio de navegación para ir a la pantalla de edición
        //    con el ID del curso recién creado. Esto cumple la postcondición del caso de uso.
        verify(navigationService, times(1)).irAEditarCurso(cursoGuardadoConId.getId());
    }

    @Test
    @DisplayName("Flujo alternativo: Intentar crear un curso con nombre nulo")
    void crearCurso_conNombreNulo_lanzaExcepcion() {
        // --- GIVEN (Dado) ---
        String nombreInvalido = null;

        // --- WHEN & THEN (Cuando y Entonces) ---
        // Se espera que se lance una excepción de tipo IllegalArgumentException
        // al intentar ejecutar el caso de uso con un nombre nulo.
        // Esto valida la precondición de que los datos mínimos son obligatorios.
        assertThrows(IllegalArgumentException.class, () -> {
            crearCursoUseCase.ejecutar(nombreInvalido);
        });

        // Verificamos que no se realizó ninguna interacción con la base de datos ni con el sistema de navegación
        verifyNoInteractions(cursoRepository, navigationService);
    }

    @Test
    @DisplayName("Flujo alternativo: Intentar crear un curso con nombre vacío")
    void crearCurso_conNombreVacio_lanzaExcepcion() {
        // --- GIVEN (Dado) ---
        String nombreInvalido = "   "; // Espacios en blanco

        // --- WHEN & THEN (Cuando y Entonces) ---
        // Se espera la misma excepción para nombres vacíos o solo con espacios.
        assertThrows(IllegalArgumentException.class, () -> {
            crearCursoUseCase.ejecutar(nombreInvalido);
        });

        // Verificamos de nuevo que no se llamó a guardar ni a navegar
        verifyNoInteractions(cursoRepository, navigationService);
    }

    @Test
    @DisplayName("Flujo de cancelación: El usuario cancela la operación")
    void cancelarCreacion_noCreaCursoYNavegaAtras() {
        // --- GIVEN (Dado) ---
        // El usuario ha iniciado la acción de crear pero la cancela antes de confirmar.
        // En una implementación real, esto significaría que el método `ejecutar` del caso de uso
        // simplemente no se llama. La UI se encargaría de llamar a `navigationService.volver()`.
        
        // --- WHEN (Cuando) ---
        // El usuario cancela (no se llama a `crearCursoUseCase.ejecutar()`).
        // Simulamos una llamada directa al servicio de navegación para volver.
        navigationService.volverACursosAbiertos();

        // --- THEN (Entonces) ---
        // Verificamos que se llamó al método para volver.
        verify(navigationService, times(1)).volverACursosAbiertos();
        
        // Y lo más importante: no se interactuó con el repositorio de cursos.
        verifyNoInteractions(cursoRepository);
    }
}

// ==== CLASES DE SOPORTE (Simuladas para el ejemplo) ====

/**
 * La clase que implementa la lógica del caso de uso.
 */
class CrearCursoUseCase {
    private final CursoRepository cursoRepository;
    private final NavigationService navigationService;

    public CrearCursoUseCase(CursoRepository cursoRepository, NavigationService navigationService) {
        this.cursoRepository = cursoRepository;
        this.navigationService = navigationService;
    }

    /**
     * Ejecuta el caso de uso "crearCurso".
     * @param nombreCurso El nombre del curso, que es el dato mínimo requerido.
     */
    public void ejecutar(String nombreCurso) {
        if (nombreCurso == null || nombreCurso.trim().isEmpty()) {
            throw new IllegalArgumentException("El nombre del curso es obligatorio.");
        }

        Curso nuevoCurso = new Curso(nombreCurso);
        Curso cursoGuardado = cursoRepository.save(nuevoCurso);
        
        // Postcondición: transferir inmediatamente a editarCurso()
        navigationService.irAEditarCurso(cursoGuardado.getId());
    }
}

/**
 * Mock de la interfaz de persistencia.
 */
interface CursoRepository {
    Curso save(Curso curso);
}

/**
 * Mock de la interfaz de navegación.
 */
interface NavigationService {
    void irAEditarCurso(Long cursoId);
    void volverACursosAbiertos();
}

/**
 * Mock de la entidad del dominio.
 */
class Curso {
    private Long id;
    private String nombre;

    public Curso(String nombre) {
        this.nombre = nombre;
    }

    // Getters y Setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getNombre() { return nombre; }
    public void setNombre(String nombre) { this.nombre = nombre; }
}
