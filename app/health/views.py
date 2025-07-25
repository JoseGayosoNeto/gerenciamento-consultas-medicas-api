from django.db import connections
from django.db.utils import OperationalError
from django.http import JsonResponse


def health_db_connection_check(request):
    # Checa a conexão com o banco de dados
    db_conn = connections['default']

    try:
        db_conn.cursor().execute('SELECT 1')
        return JsonResponse({"status": "ok"}, status=200)
    except OperationalError:
        return JsonResponse({"status": "unhealthy"}, status=503)
