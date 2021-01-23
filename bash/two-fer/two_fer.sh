#!/usr/bin/env bash
set -o errexit

main() {
  printf "One for ${1:-you}, one for me."
}

main "$@"
exit 0
