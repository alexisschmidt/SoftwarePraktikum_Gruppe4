import React, { Component } from "react";
import PropTypes from "prop-types";
import { withStyles, Paper } from "@material-ui/core";
import { withRouter } from "react-router-dom";
import ContextErrorMessage from "../dialogs/ContextErrorMessage";
import LoadingProgress from "../dialogs/LoadingProgress";
import SpoForm from "./SpoForm";
import Button from "@mui/material/Button";
import ModuleForm from "./ModuleForm";

class Administration extends Component {
  constructor(props) {
    super(props);

    //initiiere einen leeren state
    this.state = {
      tabindex: 0,
      error: null,
      loadingInProgress: false,
      spoFormIsOpen: false,
    };
  }

  // Lifecycle methode, wird aufgerufen wenn componente in den DOM eingesetzt wird
  componentDidMount() {}

  spoFormHandler = (event) => {
    if (!this.spoFormIsOpen) {
      this.setState({
        spoFormIsOpen: true,
      });
    }
  };

  spoFormClosed = (event) => {
    this.setState({
      spoFormIsOpen: false,
    });
  };

  /** Renders the component */
  render() {
    const { classes } = this.props;
    const { loadingInProgress, error, spoFormIsOpen } = this.state;

    return (
      <div className={classes.root}>
        <Paper>
          <LoadingProgress show={loadingInProgress} />
          <Button variant="contained" onClick={this.spoFormHandler}>
            SPO ERSTELLEN
          </Button>
          <SpoForm show={spoFormIsOpen} onClose={this.spoFormClosed} />
          <ContextErrorMessage
            error={error}
            contextErrorMsg={`Die Seite konnte nicht geladen werden.`}
          />
        </Paper>
      </div>
    );
  }
}

/** Component specific styles */
const styles = (theme) => ({
  root: {
    width: "100%",
  },
});

/** PropTypes */
Administration.propTypes = {
  /** @ignore */
  classes: PropTypes.object.isRequired,
  /** @ignore */
  location: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(Administration));
