set -o errexit

if curl http://localhost:8000/api/talent; then
    echo "Test 1 passed"
else
    echo "Test 1 failed"
fi