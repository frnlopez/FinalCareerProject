#!/usr/bin/env bash
# Se ejecuta en cada mensaje del usuario (hook UserPromptSubmit).
# Emite: la regla de enrutado + el estado real del repo sin commitear.
# Solo lectura. No modifica nada.
#
# Este es el punto de entrada del proyecto y el ÚNICO sitio donde se ejecuta
# `git status`: ningún subagente tiene Bash para hacerlo, a propósito.

DIR="$(cd "$(dirname "$0")" && pwd)"
REPO="$(cd "$DIR/../.." && pwd)"

cat "$DIR/leader-gate.md"

# El repo solo cuenta si su .git está en la raíz del proyecto. Si `git init`
# todavía no se ha hecho, git encontraría el repo del home y reportaría basura.
if [ -d "$REPO/.git" ]; then
    ESTADO="$(git -C "$REPO" status --short 2>/dev/null)"
    if [ -n "$ESTADO" ]; then
        RAMA="$(git -C "$REPO" branch --show-current 2>/dev/null)"
        echo
        echo "--- ESTADO DEL REPO: HAY TRABAJO SIN COMMITEAR ---"
        echo "rama ${RAMA:-?}:"
        echo "$ESTADO"
        echo
        echo "Pásale esto al leader al invocarlo. Él decide si es relevante para el mensaje"
        echo "y te lo reporta. No commitees nada por tu cuenta: eso lo hace el skill \`cierre\`,"
        echo "preguntando."
    fi
fi
