import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom";
import { Home, Room, RoomAssign, SignIn, SignUp } from "pages";
import { TopBar } from "shared";

import "normalize.css";
import "./styles.scss";

export default function App() {
  return (
    <Router>
      <div className={"viewport"}>
        <div className={"content"}>
          {/* TopBar Switch */}
          <Switch>
            <Route path="/rooms/:roomName" component={TopBar} />
            <Route component={TopBar} />
          </Switch>

          {/* Content Switch */}
          <div className="content__body">
            <Switch>
              {/* Sign In */}
              <Route path="/sign-in" component={SignIn} />

              {/* Room Paths */}
              <Route path="/rooms/:roomName/assign" component={RoomAssign} />
              <Route path="/rooms/:roomName" component={Room} />
              <Route component={Home} />
            </Switch>
          </div>
        </div>
      </div>
    </Router>
  );
}
