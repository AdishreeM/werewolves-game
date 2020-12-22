import React from "react";
import axios from "axios";
import apiClient from "apiClient";

export default class RoomAssign extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      assignmentPending: false,
      assignmentComplete: false
    };
  }

  handleYes() {
    function handleResponse(response) {
      if (response.status === 200) {
      }
    }
    this.setState({ assignmentPending: true });
    apiClient
      .post(
        serviceUrls.roomsPointedAssignX.format(this.props.match.params.roomName)
      )
      .then(response => {
        if (response.status === 200) {
          this.setState({ assignmentComplete: true, assignmentPending: false });
        }
      });
  }
  render() {
    const { assignmentComplete, assignmentPending } = this.state;
    if (!assignmentPending && !assignmentComplete)
      return (
        <div className="actual-content">
          <div className="content-heading">
            Are you sure you want to assign roles to this room?
          </div>
          <div className="button-container">
            <button onClick={() => this.handleYes()}>Yes</button>
            <button
              onClick={() => {
                this.props.history.goBack();
              }}
            >
              No
            </button>
          </div>
        </div>
      );
    if (assignmentPending) {
      return (
        <div className="content__body">
          <div className="actual-content">
            <div className="content-heading">
              Assigning roles to the players...
            </div>
          </div>
        </div>
      );
    }
    if (assignmentComplete) {
      this.props.history.goBack();
      return null;
    }
  }
}
