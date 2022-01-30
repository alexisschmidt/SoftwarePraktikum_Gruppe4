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
import { DialogTitle, Dialog, DialogActions } from "@mui/material";
import NewModuletype from "./NewModuletype";
import { DialogContent } from "@mui/material";
import NewStudyCourse from "./NewStudyCourse";
import NewExamtype from "./NewExamtype";

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
      newModuletypeOpen:false,
      newExamtypeOpen:false,
      newStudycourseOpen:false,
      newSemesterOpen:false,
      dialogtext:"",
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

  moduletypeHandler = () =>{
    this.setState({
      newModuletypeOpen:true,
      dialogtext:"neue Modulart hinzufügen"
    })
  }

  examtypeHandler = () =>{
    this.setState({
      newExamtypeOpen:true,
      dialogtext:"neues Prüfungsart hinzufügen"
    })
  }

  studycourseHandler = () =>{
    this.setState({
      newStudycourseOpen:true,
      dialogtext:"neuen Studiengang hinzufügen"
    })
  }

  semesterHandler = () =>{
    this.setState({
      newSemesterOpen:true,
      dialogtext:"neues Prüfungsart hinzufügen"
    })
  }
  

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
  closeDialog = () =>{
    this.setState({
      newModuletypeOpen:false,
      newExamtypeOpen:false,
      newSemesterOpen:false,
      newStudycourseOpen:false,
      dialogtext:"",
    })
  }

  /** Renders the component */
  render() {
    const { classes } = this.props;
    const { loadingInProgress, error, spoFormIsOpen, moduleFormOpen, modulepartFormOpen, newModuletypeOpen, newStudycourseOpen, newSemesterOpen, newExamtypeOpen, dialogtext } =
      this.state;

    return (
      <div className={classes.root}>
        <Paper>
          <LoadingProgress show={loadingInProgress} />
          
          <Button variant="contained" onClick={this.modulepartFormHandler}>
            Modulteile ERSTELLEN
          </Button>
          <Button variant="contained" onClick={this.moduleFormHandler}>
            Module ERSTELLEN
          </Button>
          <Button variant="contained" onClick={this.spoFormHandler}>
            SPO ERSTELLEN
          </Button>
          <Button variant="contained" onClick={this.moduletypeHandler}>
            Moduletype erstellen
          </Button>
          <Button variant="contained" onClick={this.examtypeHandler}>
            Prüfungsart erstellen
          </Button>
          <Button variant="contained" onClick={this.studycourseHandler}>
            Studiengang erstellen
          </Button>
          <Button variant="contained" onClick={this.semesterHandler}>
            Semester erstellen
          </Button>

          
          <ModulepartForm show={modulepartFormOpen} onClose={this.modulepartFormClosed} />
          <ModuleForm show={moduleFormOpen} onClose={this.moduleFormClosed} />
          <SpoForm show={spoFormIsOpen} onClose={this.spoFormClosed} />

          <Dialog open={newModuletypeOpen||newStudycourseOpen||newSemesterOpen||newExamtypeOpen} onclose={this.closeDialog}>
            <DialogTitle>{dialogtext}</DialogTitle>
            <DialogContent>
            {newModuletypeOpen?<NewModuletype handleClose={this.closeDialog}/>:null}
            {newExamtypeOpen?<NewExamtype handleClose={this.closeDialog}/>:null}
            {newStudycourseOpen?<NewStudyCourse handleClose={this.closeDialog}/>:null}
            {newSemesterOpen?<newSemester handleClose={this.closeDialog}/>:null}

            </DialogContent>
            <DialogActions>
              <Button onClick={this.closeDialog}>Schließen</Button>
            </DialogActions>
          </Dialog>

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
