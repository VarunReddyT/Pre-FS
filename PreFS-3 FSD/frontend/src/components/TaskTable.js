import React, { useState } from 'react';

function TaskTable({ tasks, onUpdateTask, onDeleteTask }) {
  const [editingId, setEditingId] = useState(null);
  const [editFormData, setEditFormData] = useState({});
  const [message, setMessage] = useState(''); // Message for actions

  // Handle input changes during editing
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setEditFormData({ ...editFormData, [name]: value });
  };

  // Start editing a row
  const handleEditClick = (task) => {
    setEditingId(task._id);
    setEditFormData(task);
    setMessage('');
  };

  // Save the edited task
  const handleSaveClick = async () => {
    const msg = await onUpdateTask(editingId, editFormData);
    setMessage(msg);
    setEditingId(null);
  };

  // Cancel editing
  const handleCancelClick = () => {
    setEditingId(null);
    setMessage('Editing cancelled.');
  };

  // Delete a task
  const handleDeleteClick = async (id) => {
    const msg = await onDeleteTask(id);
    setMessage(msg);
  };

  return (
    <>
      {/* Message Display */}
      {message && <p className="text-info mb-3">{message}</p>}

      <table className="table table-striped">
        <thead>
          <tr>
            <th>Title</th>
            <th>Description</th>
            <th>Status</th>
            <th>Due Date</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {tasks.map((task) => (
            editingId === task._id ? (
              <tr key={task._id}>
                <td>
                  <input
                    type="text"
                    className="form-control"
                    name="title"
                    value={editFormData.title}
                    onChange={handleInputChange}
                  />
                </td>
                <td>
                  <input
                    type="text"
                    className="form-control"
                    name="description"
                    value={editFormData.description}
                    onChange={handleInputChange}
                  />
                </td>
                <td>
                  <select
                    className="form-control"
                    name="status"
                    value={editFormData.status}
                    onChange={handleInputChange}
                  >
                    <option value="Pending">Pending</option>
                    <option value="In Progress">In Progress</option>
                    <option value="Completed">Completed</option>
                  </select>
                </td>
                <td>
                  <input
                    type="date"
                    className="form-control"
                    name="dueDate"
                    value={editFormData.dueDate.split('T')[0]}
                    onChange={handleInputChange}
                  />
                </td>
                <td>
                  <button className="btn btn-success btn-sm me-2" onClick={handleSaveClick}>
                    Save
                  </button>
                  <button className="btn btn-secondary btn-sm" onClick={handleCancelClick}>
                    Cancel
                  </button>
                </td>
              </tr>
            ) : (
              <tr key={task._id}>
                <td>{task.title}</td>
                <td>{task.description}</td>
                <td>{task.status}</td>
                <td>{new Date(task.dueDate).toLocaleDateString()}</td>
                <td>
                  <button className="btn btn-warning btn-sm me-2" onClick={() => handleEditClick(task)}>
                    Edit
                  </button>
                  <button className="btn btn-danger btn-sm" onClick={() => handleDeleteClick(task._id)}>
                    Delete
                  </button>
                </td>
              </tr>
            )
          ))}
        </tbody>
      </table>
    </>
  );
}

export default TaskTable;
