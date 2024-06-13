# from django.core.management.base import BaseCommand
# from django.db import connection

# class Command(BaseCommand):
#     help = 'Check database connection'

#     def handle(self, *args, **kwargs):
#         try:
#             connection.ensure_connection()
#             self.stdout.write(self.style.SUCCESS('Connection to MySQL is successful'))
#         except Exception as e:
#             self.stdout.write(self.style.ERROR(f'Connection failed: {e}'))


# # t = Command()
# # t.handle()
