
# returning the date property
def get_date(post):
     return post.get('date')

# returning the modified list
def get_modified_list(posts: list, operation: str):
      modified_list =  map(data_add_modifier, posts) if operation.lower() == 'add' else map(data_delete_modifier, posts)
      return modified_list


def data_add_modifier(post):
       post['class'] = 'card-img-top'
       return post

def data_delete_modifier(post):
        if('class' in post):
          del post['class']
        return post