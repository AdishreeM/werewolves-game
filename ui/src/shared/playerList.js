import React from "react";

export default function PlayerList(props) {
  function displayColumn(players, showRoles = false, roleFirst = false) {
    const entries = players.map(player => {
      const nameDiv = (
        <div
          className={
            "player-list__column__entry__name" +
            (showRoles ? " showRoles" : " hideRoles")
          }
        >
          {player.name}
        </div>
      );
      const roleDiv = (
        <div
          className={
            "player-list__column__entry__role" +
            (showRoles ? " showRoles" : " hideRoles")
          }
        >
          {player.role}
        </div>
      );
      return (
        <div
          className={
            "player-list__column__entry" +
            (showRoles ? " showRoles" : " hideRoles")
          }
        >
          {roleFirst ? (
            <>
              {roleDiv}
              {nameDiv}
            </>
          ) : (
            <>
              {nameDiv}
              {roleDiv}
            </>
          )}
        </div>
      );
    });

    return <div className="player-list__column">{entries}</div>;
  }
  function splitToCols(players, showRoles) {
    if (players.length < 6) {
      return displayColumn(players);
    } else {
      const breakpoint = Math.ceil(players.length / 2);
      return (
        <>
          {displayColumn(players.slice(0, breakpoint), showRoles, true)}
          {displayColumn(players.slice(breakpoint), showRoles)}
        </>
      );
    }
  }
  return (
    <div className="player-list">
      {splitToCols(props.players, props.showRoles)}
    </div>
  );
}
