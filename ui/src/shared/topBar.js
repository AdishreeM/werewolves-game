import React from "react";
import { Link } from "react-router-dom";
import classNames from "classnames";

export default class TopBar extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      hamburgerMenuActive: false
    };
  }
  closeHamburgerMenu = () => {
    this.setState({ hamburgerMenuActive: false });
  };
  render() {
    return (
      <>
        <div className={"content__topbar"}>
          <div className={"content__topbar__logo"}>Wolves</div>
          {this.props.match &&
            this.props.match.params &&
            this.props.match.params.roomName && (
              <div className="content__topbar__roomName">
                {this.props.match.params.roomName}
              </div>
            )}
          {this.state.hamburgerMenuActive ? (
            <div
              className={"content__topbar__close"}
              onClick={() => {
                this.setState({ hamburgerMenuActive: false });
              }}
            >
              X
            </div>
          ) : (
            <div
              className={"content__topbar__hamburger"}
              onClick={() => {
                this.setState({ hamburgerMenuActive: true });
              }}
            ></div>
          )}
        </div>
        <div
          className={classNames("hamburger-menu", {
            "hamburger-menu--active": this.state.hamburgerMenuActive
          })}
        >
          <Link to="/sign-in" onClick={this.closeHamburgerMenu}>
            Sign In
          </Link>
          <Link to="/sign-up" onClick={this.closeHamburgerMenu}>
            Sign Up
          </Link>
          <Link to="/about" onClick={this.closeHamburgerMenu}>
            About
          </Link>
          <Link to="/contribute" onClick={this.closeHamburgerMenu}>
            Contribute
          </Link>
        </div>
      </>
    );
  }
}
