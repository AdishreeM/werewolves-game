import React from "react";
import {login} from "apiClient";

export default class SignIn extends React.Component {
  constructor(props) {
    super(props);
    this.state = { userNameInputValue: null, passwordInputValue: null, failed: false };
  }
  handleSignIn()
  {
      const {userNameInputValue, passwordInputValue} = this.state;
      login(userNameInputValue, passwordInputValue, this.onLoginSuccess.bind(this), this.onLoginFailure.bind(this));
  }

  onLoginSuccess() {
      console.log("loggedin");
      this.props.history.goBack()
  }

  onLoginFailure() {
    this.setState({failed: true})
  }

  render() {
    return (
      <div className="actual-content">
        <input
          className={"username-input"}
          placeholder="Username"
          value={this.state.userNameInputValue}
          onChange={event =>
            this.setState({
              userNameInputValue: event.target.value
            })
          }
        />
        <input
          className={"password-input"}
          placeholder="Password"
          value={this.state.passwordInputValue}
          onChange={event =>
            this.setState({
              passwordInputValue: event.target.value
            })
          }
        />
        <div className="button-container">
          <button onClick={() => this.handleSignIn()}>
            Sign In
          </button>
        </div>
        { this.state.failed && <h1>Chutiya!</h1>}
      </div>
    );
  }
}
