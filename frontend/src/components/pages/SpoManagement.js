import React, { Component } from "react";
import PropTypes from "prop-types";
import { withStyles, Paper } from "@material-ui/core";
import { withRouter } from "react-router-dom";
import ContextErrorMessage from "../dialogs/ContextErrorMessage";
import LoadingProgress from "../dialogs/LoadingProgress";
import SpoForm from "./SpoForm";
import Button from "@mui/material/Button";
import ModuleForm from "./ModuleForm";
import ModulepartForm from "./ModulepartForm";

class Administration extends Component {
  constructor(props) {
    super(props);

    //initiiere einen leeren state
    this.state = {
      tabindex: 0,
      error: null,
      loadingInProgress: false,
      spoFormIsOpen: false,
      moduleFormOpen: false,
      modulepartFormOpen: false,
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
  moduleFormHandler = (event) => {
    if (!this.moduleFormOpen) {
      this.setState({
        moduleFormOpen: true,
      });
    }
  };

  modulepartFormHandler = (event) => {
    if (!this.modulepartFormOpen) {
      this.setState({
        modulepartFormOpen: true,
      });
    }
  };

  spoFormClosed = (event) => {
    this.setState({
      spoFormIsOpen: false,
    });
  };
  moduleFormClosed = (event) => {
    this.setState({
      moduleFormOpen: false,
    });
  };
  modulepartFormClosed = (event) => {
    this.setState({
      modulepartFormOpen: false,
    });
  };

  /** Renders the component */
  render() {
    const { classes } = this.props;
    const { loadingInProgress, error, spoFormIsOpen, moduleFormOpen, modulepartFormOpen } =
      this.state;

    return (
      <div className={classes.root}>
        <Paper>
          <LoadingProgress show={loadingInProgress} />
          <Button variant="contained" onClick={this.spoFormHandler}>
            SPO ERSTELLEN
          </Button>
          <Button variant="contained" onClick={this.moduleFormHandler}>
            Module ERSTELLEN
          </Button>
          <Button variant="contained" onClick={this.modulepartFormHandler}>
            Modulteile ERSTELLEN
          </Button>

          <SpoForm show={spoFormIsOpen} onClose={this.spoFormClosed} />
          <ModuleForm show={moduleFormOpen} onClose={this.moduleFormClosed} />
          <ModulepartForm show={modulepartFormOpen} onClose={this.modulepartFormClosed} />


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
