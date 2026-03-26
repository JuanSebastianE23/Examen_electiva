# Estrategia de Ramas

## Ramas Principales

### main
- Rama de producción
- Código estable y probado
- Solo se actualiza desde `dev` mediante merge

### dev
- Rama de desarrollo principal
- Base para todas las features
- Integración continua de nuevas funcionalidades

## Ramas de Trabajo

### feature/*
Crear desde `dev` para nuevas funcionalidades:
```bash
git checkout dev
git pull origin dev
git checkout -b feature/nombre-funcionalidad
```

### hotfix/*
Crear desde `main` para correcciones urgentes:
```bash
git checkout main
git pull origin main
git checkout -b hotfix/descripcion-fix
```

### release/*
Crear desde `dev` para preparar releases:
```bash
git checkout dev
git checkout -b release/v1.0.0
```

## Flujo de Trabajo

1. Desarrollar en `feature/*` o `hotfix/*`
2. Hacer commits frecuentes
3. Merge a `dev` cuando esté completo
4. Probar en `dev`
5. Merge a `main` cuando esté listo para producción
