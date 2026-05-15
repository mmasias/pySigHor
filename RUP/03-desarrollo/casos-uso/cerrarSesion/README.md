# pySigHor > cerrarSesion > Desarrollo
> |[🏠️](/RUP/README.md)|[ 📊](https://raw.githubusercontent.com/mmasias/pySigHor/diseño-fastapi-react/images/RUP/99-seguimiento/diagrama-contexto-administrador.svg)|[Detalle](/RUP/00-casos-uso/02-detalle/cerrarSesion/README.md)|[Análisis](/RUP/01-analisis/casos-uso/cerrarSesion/README.md)|[Diseño](/RUP/02-diseño/casos-uso/cerrarSesion/README.md)|**Desarrollo**|Pruebas|
> |-|-|-|-|-|-|-|

- **Frontend:** [context/AuthContext.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/context/AuthContext.tsx) · [components/Layout.tsx](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/components/Layout.tsx) · [services/api.ts](https://github.com/mmasias/pySigHor/blob/diseño-fastapi-react/frontend/src/services/api.ts)

Operación puramente cliente: no requiere endpoint de backend. JWT stateless — basta con eliminar el token del almacenamiento local.

## Implementación

```ts
// api.ts
logout: () => {
  localStorage.removeItem('token');
  localStorage.removeItem('user');
}
```

```ts
// AuthContext.tsx
const logout = () => {
  authService.logout();
  setUser(null);        // isAuthenticated pasa a false → ProtectedRoute redirige a /login
};
```

El botón está en el `AppBar` de `Layout.tsx` (icono `LogoutIcon`). Al hacer clic llama a `logout()` del contexto.
