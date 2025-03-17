from sqlalchemy import create_engine

db_url = "postgresql://postgres.ytmcxjaikxgpfwvxkyyg:Tricolor1020%40%40%40@aws-0-sa-east-1.pooler.supabase.com:5432/postgres"

try:
    engine = create_engine(db_url)
    conn = engine.connect()
    print("Conexão bem-sucedida!")
    conn.close()
except Exception as e:
    print(f"Erro ao conectar: {e}")
