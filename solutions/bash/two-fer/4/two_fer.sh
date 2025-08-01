#!/usr/bin/env bash
set -o errexit

main() {
  printf "One for %s, one for me." "${1:-you}"
}

main "$@"
exit 0
