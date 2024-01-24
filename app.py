from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for demonstration purposes
data = [
    {'id': 1, 'name': 'Post 1'},
    {'id': 2, 'name': 'Post 2'},
    {'id': 3, 'name': 'Post 3'},
]

# Get all posts
@app.route('/posts', methods=['GET'])
def get_all_posts():
    return jsonify({'posts': data})

# Get a specific post
@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = next((item for item in data if item['id'] == post_id), None)
    if post:
        return jsonify({'post': post})
    else:
        return jsonify({'error': 'Post not found'}), 404

# Create a new post
@app.route('/posts', methods=['POST'])
def create_post():
    new_post = {'id': len(data) + 1, 'name': request.json['name']}
    data.append(new_post)
    return jsonify({'post': new_post}), 201

# Update a post
@app.route('/posts/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = next((item for item in data if item['id'] == post_id), None)
    if post:
        post['name'] = request.json['name']
        return jsonify({'post': post})
    else:
        return jsonify({'error': 'Post not found'}), 404

# Delete a post
@app.route('/posts/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    global data
    data = [item for item in data if item['id'] != post_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)
