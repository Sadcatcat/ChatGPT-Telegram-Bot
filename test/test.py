my_list = [
    {"role": "admin", "content": "This is admin content."},
    {"role": "user", "content": "This is user content."}
]

content_list = [item["content"] for item in my_list]
print(content_list)

engine = "gpt-3.5-turbo-1106"
truncate_limit = (
    30500
    if "gpt-4-32k" in engine
    else 6500
    if "gpt-4" in engine
    else 14500
    if "gpt-3.5-turbo-16k" in engine or "gpt-3.5-turbo-1106" in engine
    else 98500
    if ("claude-2-web" or "claude-2") in engine
    else 3400
)

print(truncate_limit)