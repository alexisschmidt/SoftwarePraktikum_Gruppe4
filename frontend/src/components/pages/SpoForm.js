import React, { Component } from "react";
import PropTypes from "prop-types";
import ListItemIcon from '@mui/material/ListItemIcon';
import {
  Button,
  IconButton,
  Dialog,
  DialogContent,
  DialogTitle,
  DialogActions,
  TextField, 
  Stepper,
  Step,
  StepLabel, 
  Checkbox,
  ListItem,
  Grid, 
  ListItemText,
  Paper,
  List,
} from "@mui/material";
import CloseIcon from "@material-ui/icons/Close";
import ContextErrorMessage from "../dialogs/ContextErrorMessage";
import LoadingProgress from "../dialogs/LoadingProgress";

import Spobo from "../../api/BusinessObjects/Spobo";
import API from "../../api/API";

class SpoForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      
      id: null,
      name: "",
      nameValidationFailed: false,
      nameEdited: false,

      title: null,
      titleValidationFailed: false,
      titleEdited: false,

      start_semester: null,
      start_semesterValidationFailed: false,
      start_semesterEdited: false,

      end_semester: null,
      end_semesterValidationFailed: false,
      end_semesterEdited: false,

      studyCourse: null,
      studyCourseValidationFailed: false,
      studyCourseEdited: false,

      //wurde importiert aus der Main

      addingError: null,
      addingInProgress: false,

      updatingError: null,
      updatingInProgress: false,

      //Iterator für den Stepper
      activeStep: 0,

      //Variablen für die Modulauswahl
      module:[],
      moduleInSPO: [],
      checked: [],
    };
    this.baseState = this.state;
  }
  componentDidMount = () =>{
    this.getInfos()
  }

  addSpo = () => {
    let newSpo = new Spobo();
    newSpo.setID(0);
    newSpo.setName(this.state.name);
    newSpo.setTitle(this.state.title);
    newSpo.setStart_semester(this.state.start_semester);
    newSpo.setEnd_semester(this.state.end_semester);
    newSpo.setStudycourse(this.state.studycourse);

    //die Module müssen zur spo hinzugefügt werden, entweder durch eine update methode fürs modul im backend oder indem die module direkt im spobo hinzugefügt werden
    //let modulIDs=this.state.moduleInSPO.map(module => module.getID());
    //newSPO.setModules(modulIDs);

    API.getAPI()
      .addSpo(newSpo)
      .then((spo) => {
        this.setState(this.baseState);
        this.props.onClose(spo); //Aufrufen parent in backend
      })
      .catch((e) =>
        this.setState({
          addingInProgress: false,
          addingError: e,
        })
      );
    // Ladeanimation einblenden
    this.setState({
      addingProgress: true,
      addingError: null,
    });
  };

  // Validierung der Textfeldaenderungen
  textFieldValueChange = (event) => {
    const value = event.target.value;

    let error = false;
    if (value.trim().length === 0) {
      error = true;
    }
    this.setState({
      [event.target.id]: event.target.value,
      [event.target.id + "ValidationFailed"]: error,
      [event.target.id + "Edited"]: true,
    });
  };

  numberValueChange = (event) => {
    const value = event.target.value;
    const re = /^[0-9]{1,10}$/;

    let error = false;
    if (value.trim().length === 0) {
      error = true;
    }
    if (re.test(event.target.value) === false) {
      error = true;
    }

    this.setState({
      [event.target.id]: event.target.value,
      [event.target.id + "ValidationFailed"]: error,
      [event.target.id + "Edited"]: true,
    });
  };

  getInfos = () => {
    if (this.props.spo) {
      const { spo } = this.props;

      this.setState({
        id: spo.id,
        name: spo.name,
        title: spo.title,
        start_semester: spo.start_semester,
        end_semester: spo.end_semester,
        semester: spo.semester,
        studyCourse: spo.studyCourse,
        //anpassen von id?
      });
    }
  };
  getModule = () => {
    const { spo } = this.props;
    //TODO: Überprüfen, ob diese Methode wirklich alle Module aus der DB holt
    API.getAPI().getAllModule().then((response) => {
      if (spo) {
        //TODO: anpassen auf die passende Methode in API
        API.getAPI().getAllModuleForSPO(spo.id).then((module) => {
          //alle module die in der spo sind aus der response entfernen
          let moduleOhneSpo = response.filter((m) => {
            //Array.some überprüft, ob ein Element in dem Array vorkommt, wenn das Element schon in der Spo vorhanden ist, wird es dann aus der response rausgefiltert
            return !module.some((m2) => m2.id === m.id);
          });
          this.setState({
            moduleInSPO: module,
            module: moduleOhneSpo,
          });
        });
      }
      else{
        this.setState({
          module: response,
        });
      }
    });
    
  };

  handleClose = () => {
    this.setState(this.baseState);
    this.props.onClose(null);
  };
  //Stepper Methoden
  handleBack = () => {
    this.setState({
      activeStep: 0,
    });
  };
  handleNext = () => {
    const {spo} = this.props;
    if (this.state.activeStep === 0){
      this.getModule()
      this.setState({
        activeStep: 1,
      })}
    else if (this.state.activeStep === 1){
    spo? this.updateSpo() : this.addSpo();
    }
    
  };

  //Module hinzufügen Methoden
  handleToggle = (value) => () => {
    //überprüfen ob das value schon in dem checked array ist, wenn es drin ist wird es entfernt und ansonsten hinzugefügt
    const { checked } = this.state;
    const currentIndex = checked.indexOf(value);
    const newChecked = checked;

    if (currentIndex === -1) {
      newChecked.push(value);
    } else {
      newChecked.splice(currentIndex, 1);
    }
    this.setState({
      checked: newChecked,
    });
  }

  handleAllLeft = () => {
    const newModule = this.state.module;
    //alle module aus this.state.moduleInSPo in newModule hinzufügen
    this.state.moduleInSPO.forEach((m) => {
      newModule.push(m);
    });
    this.setState({
      checked: [],
      moduleInSPO: [],
      module: newModule,
    });
  }
  handleAllRight = () => {
    const newModule = this.state.moduleInSPO;
    //alle module aus this.state.module in newModule hinzufügen
    this.state.module.forEach((m) => {
      newModule.push(m);
    });
    this.setState({
      checked: [],
      module: [],
      moduleInSPO: newModule,
    });
  }
  handleCheckedLeft = () => {
    const newModule = this.state.module;
    //alle checked module aus this.state.moduleInSPO in newModule hinzufügen
    this.state.moduleInSPO.forEach((m) => {
      if (this.state.checked.includes(m.id)) {
        newModule.push(m);
      }
    });
    this.setState({
      checked: [],
      moduleInSPO: newModule,
      module: this.state.module.filter((m) => !this.state.checked.includes(m.id)),
    });
  }
  handleCheckedRight = () => {
    const newModule = this.state.moduleInSPO;
    //alle checked module aus this.state.module in newModule hinzufügen
    this.state.module.forEach((m) => {
      if (this.state.checked.includes(m.id)) {
        newModule.push(m);
      }
    });
    this.setState({
      checked: [],
      module: newModule,
      moduleInSPO: this.state.moduleInSPO.filter((m) => !this.state.checked.includes(m.id)),
    });
  }

  intersection = (checkedarray, module) => {
    //überprüft ob ein modul in dem checkedarray vorhanden ist
    const modulIDs = module.map((m) => m.id);
    return checkedarray.filter((c) => modulIDs.tabIndexOf(c) !== -1);
  }




  renderTextfields() {
    const {name,nameValidationFailed, title, titleValidationFailed, start_semester,start_semesterValidationFailed, end_semester, end_semesterValidationFailed,studyCourse, studyCourseValidationFailed} = this.state;
    return (
      <>
      <form noValidate autoComplete="off">
            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              margin="small"
              id="name"
              label="Sponame"
              variant="outlined"
              value={name}
              onChange={this.textFieldValueChange}
              error={nameValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
              margin="small"
              id="title"
              label="Title"
              variant="outlined"
              value={title}
              onChange={this.textFieldValueChange}
              error={titleValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
              margin="small"
              id="start_semester"
              label="Start Semester"
              variant="outlined"
              value={start_semester}
              onChange={this.numberValueChange}
              error={start_semesterValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
              margin="small"
              id="end_semester"
              label="End Semester"
              variant="outlined"
              value={end_semester}
              onChange={this.numberValueChange}
              error={end_semesterValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
              margin="small"
              id="studyCourse"
              label="StudyCourse"
              variant="outlined"
              value={studyCourse}
              onChange={this.textFieldValueChange}
              error={studyCourseValidationFailed}
            />
          </form>
      </>
    );
  }
  renderAddModul() {
    const {module, moduleInSPO, checked} = this.state

  //Die Module, die jeweils auf der linken und rechten Seite ausgewählt sind
  const leftChecked = this.intersection(checked, module);
  const rightChecked = this.intersection(checked, moduleInSPO);

    const customList = (items) => (
      <Paper sx={{ width: 200, height: 230, overflow: 'auto' }}>
        <List dense component="div" role="list">
          {items.map((m) => {
            const labelId = `transfer-list-item-${m.id}-label`;
  
            return (
              <ListItem
                key={m.id}
                role="listitem"
                button
                onClick={this.handleToggle(m.id)}
              >
                <ListItemIcon>
                  <Checkbox
                    checked={checked.indexOf(m.id) !== -1}
                    tabIndex={-1}
                    disableRipple
                    inputProps={{
                      'aria-labelledby': labelId,
                    }}
                  />
                </ListItemIcon>
                <ListItemText id={labelId} primary={`${m.name}`} />
              </ListItem>
            );
          })}
          <ListItem />
        </List>
      </Paper>
    );
    return (
      <>
          <Grid container spacing={2} justifyContent="center" alignItems="center">
      <Grid item>{customList(module)}</Grid>
      <Grid item>
        <Grid container direction="column" alignItems="center">
          <Button
            sx={{ my: 0.5 }}
            variant="outlined"
            size="small"
            onClick={this.handleAllRight}
            disabled={module.length === 0}
            aria-label="move all right"
          >
            ≫
          </Button>
          <Button
            sx={{ my: 0.5 }}
            variant="outlined"
            size="small"
            onClick={this.handleCheckedRight}
            disabled={leftChecked.length === 0}
            aria-label="move selected right"
          >
            &gt;
          </Button>
          <Button
            sx={{ my: 0.5 }}
            variant="outlined"
            size="small"
            onClick={this.handleCheckedLeft}
            disabled={rightChecked.length === 0}
            aria-label="move selected left"
          >
            &lt;
          </Button>
          <Button
            sx={{ my: 0.5 }}
            variant="outlined"
            size="small"
            onClick={this.handleAllLeft}
            disabled={moduleInSPO.length === 0}
            aria-label="move all left"
          >
            ≪
          </Button>
        </Grid>
      </Grid>
      <Grid item>{customList(moduleInSPO)}</Grid>
    </Grid>
      </>
    );
  }
  render() {
    const { show, spo } = this.props;

    let {
     

      nameValidationFailed,
      nameEdited,

      titleValidationFailed,
      titleEdited,

      
      start_semesterValidationFailed,
      start_semesterEdited,

      end_semesterValidationFailed,
      end_semesterEdited,

      studyCourseValidationFailed,
      studyCourseEdited,

    

      addingInProgress,
      addingError,
      updatingInProgress,
      updatingError,
      
      activeStep,
    } = this.state;

    let title = "";
    let header = "";

    if (spo) {
      // Projekt objekt true, somit ein edit
      title = `Spo "${spo.name}" erstellen`;
      header = ["Neue Spo Daten einfügen", "Module bearbeiten"];
    } else {
      title = "Erstelle eine neue Spo";
      header = ["Spo Daten einfügen","Module auswählen"];
    }

    return show ? (
      <Dialog
        open={show}
        onClose={this.handleClose}
        maxWidth="xs"
        fullWidth
      >
        <DialogTitle>
          {title}
          <IconButton onClick={this.handleClose}>
            <CloseIcon />
          </IconButton>
        </DialogTitle>
        <DialogContent>
          <Stepper activeStep={activeStep}>
            {header.map((label, index) => (
              <Step key={index}>
                <StepLabel>{label}</StepLabel>
              </Step>
            ))}
          </Stepper>
          {activeStep===0? this.renderTextfields():this.renderAddModul()}
          <LoadingProgress show={addingInProgress || updatingInProgress} />
          {
            // Show error message in dependency of Projektart prop
            spo ? (
              <ContextErrorMessage
                error={updatingError}
                contextErrorMsg={`The Spo ${spo.getID()} could not be updated.`}
                onReload={this.updateSpo}
              />
            ) : (
              <ContextErrorMessage
                error={addingError}
                contextErrorMsg={`The Spo could not be added.`}
                onReload={this.addSpo}
              />
            )
          }
        </DialogContent>
        <DialogActions>
          {activeStep===0?
          <Button onClick={this.handleClose} color="secondary">
            Abbrechen
          </Button>
          :
          <Button onClick={this.handleBack} color="secondary">
            Zurück
          </Button>
          }
          {
            // If a Projekt is given, show an update button, else an add button
            spo ? (
              <Button
                disabled={
                  nameValidationFailed ||
                  titleValidationFailed ||
                  start_semesterValidationFailed ||
                  end_semesterValidationFailed ||
                  studyCourseValidationFailed
                }
                variant="contained"
                onClick={this.handleNext}
                color="primary"
              >
                {activeStep===0? "Weiter":"Speichern"}
              </Button>
            ) : (
              <Button
                disabled={
                  nameValidationFailed ||
                  !nameEdited ||
                  titleValidationFailed ||
                  !titleEdited ||
                  start_semesterValidationFailed ||
                  !start_semesterEdited ||
                  end_semesterValidationFailed ||
                  !end_semesterEdited ||
                  studyCourseValidationFailed ||
                  !studyCourseEdited
                }
                variant="contained"
                onClick={this.handleNext}
                color="primary"
              >
                {activeStep===0? "Weiter":"Hinzufügen"}
              </Button>
            )
          }
        </DialogActions>
      </Dialog>
    ) : null;
  }
}

/** PropTypes */
SpoForm.propTypes = {
  /** If true, the form is rendered */
  show: PropTypes.bool.isRequired,
  /**
   * Handler function which is called, when the dialog is closed.
   * Sends the edited or created projektBO's as parameter or null, if cancel was pressed.
   *
   * Signature: onClose(ProjektBO's projekt);
   */
  onClose: PropTypes.func.isRequired,
};

export default SpoForm;