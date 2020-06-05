

class db_middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        import time
        from django.db import connection
        start = time.time()
        initial_count = len(connection.queries)
        response = self.get_response(request)
        end = time.time()
        final_count = len(connection.queries)
        print("\n")
        print(f"time_executed.....{end-start}seconds")
        print(f"total db hits {final_count-initial_count}...")
        print("\n\n\n")
        return response