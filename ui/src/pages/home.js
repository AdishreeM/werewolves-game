import React from "react";
import axios from "axios";

export default class Home extends React.Component {
  static pendingFlags = {
    none: null,
    join: "JOIN",
    start: "START"
  };

  constructor(props) {
    super(props);

    this.state = {
      roomNameInputValue: "",
      pending: Home.pendingFlags.none,
      inputError: null
    };
  }
  handleStart() {
    const { roomNameInputValue } = this.state;
    if (roomNameInputValue === "") {
      this.setState({ inputError: "The emptiness is scaring me" });
      setTimeout(() => this.setState({ inputError: null }), 500);
    } else {
      console.log(`Creating room ${roomNameInputValue}...`);
      this.setState({ pending: Home.pendingFlags.start });
      axios
        .get(serviceUrls.startRoom)
        .then(response => {
          if (response.status === 200) {
            this.props.history.push(`/rooms/${response.data.roomName}`);
          } else {
            console.log("non 200 status");
          }
        })
        .catch(error => {
          console.log(error);
          if (error.response.status === 500) {
            this.setState({
              inputError: "This room is taken, please try another one",
              pending: Home.pendingFlags.none
            });
          } else {
            this.setState({
              inputError:
                "Oops, something isn't right. It's not you, it's me :(",
              pending: Home.pendingFlags.none
            });
          }
        });
    }
  }

  handleJoin() {
    const { roomNameInputValue } = this.state;
    if (roomNameInputValue === "") {
      this.setState({ inputError: "The emptiness is scaring me" });
      setTimeout(() => this.setState({ inputError: null }), 500);
    } else {
      console.log(`trying to join room ${roomNameInputValue}...`);
      this.setState({ pending: Home.pendingFlags.join });
      axios
        .get(serviceUrls.joinRoom)
        .then(response => {
          if (response.data.exists === true) {
            this.props.history.push(`/rooms/${response.data.roomName}`);
          } else {
            this.setState({
              inputError: "This room doesn't exists :(",
              pending: Home.pendingFlags.none
            });
          }
        })
        .catch(error => {
          console.log(error);
          this.setState({
            inputError: "Oops, something isn't right. It's not you, it's me :(",
            pending: Home.pendingFlags.none
          });
        });
    }
  }
  render() {
    return (
      <div className="actual-content">
        <input
          className={
            "room-name-input" +
            (this.state.inputError ? " room-name-input--invalid" : "")
          }
          placeholder="room-name"
          value={this.state.roomNameInputValue}
          onChange={event =>
            this.setState({
              roomNameInputValue: event.target.value,
              inputError: null
            })
          }
        />
        <div className="button-container">
          <button onClick={() => this.handleStart()}>Start</button>
          <button onClick={() => this.handleJoin()}>Join</button>
        </div>
      </div>
    );
  }
}
