insert into user_key_assoc(user_id, relation_id)
select uid, relation_id
from users
inner join keywords
where users.uid = "admin" and keywords.keyword = "ad"