import os

pwd = '########'
user_id = 'postgres.enwlropbugxjthknxsex'
server = 'aws-0-ap-southeast-1.pooler.supabase.com'
db = 'postgres'
driver = 'org.postgresql.Driver'
server_target = "aws-0-us-west-1.pooler.supabase.com"

src_url = f"jdbc:postgresql://{server}:5432/{db}?user={user_id}&password={pwd}"

 
# target connection
target_url = f"jdbc:postgresql://aws-0-us-west-1.pooler.supabase.com:5432/postgres?user=postgres.bjuxjncxeiihnabfmqmp&password={pwd}"
