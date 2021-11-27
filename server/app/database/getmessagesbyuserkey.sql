select contents
from messages
inner join keywords
inner join user_key_assoc
where user_key_assoc.relation_id = keywords.relation_id and keywords.mid = messages.mid