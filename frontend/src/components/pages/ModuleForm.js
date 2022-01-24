import React, { Component } from "react";
import PropTypes from "prop-types";
import Modulebo from "../../api/BusinessObjects/Modulebo";
import API from "../../api/API";
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
import ContextErrorMessage from "./ContextErrorMessage";
import LoadingProgress from "./LoadingProgress";

class ModuleForm extends Component {
  constructor(props) {
    super(props);
      this.state = {

      id: null,
      name: "",
      nameValidationFailed: false,
      nameEdited: false,

      edvnr: null,
      edvnrValidationFailed: false,
      edvnrEdited: false,

      ects: null,
      ectsValidationFailed: false,
      ectsEdited: false,

      workload: null,
      workloadValidationFailed: false,
      workloadEdited: false,

      type: null,
      typeValidationFailed: false,
      typeEdited: false,

      requirement: null,
      requirementValidationFailed: false,
      requirementEdited: false,

      outcome: null,
      outcomeValidationFailed: false,
      outcomeEdited: false,

      examtype: null,
      examtypeValidationFailed: false,
      examtypeEdited: false,

      instructor: null,
      instructorValidationFailed: false,
      instructorEdited: false,

      addingError: null,
      addingInProgress: false,

      updatingError: null,
      updatingInProgress: false,

       //Iterator für den Stepper
       activeStep: 0,

       //Variablen für die Modulauswahl
       modulepart:[],
       modulepartInModule: [],
       checked: [],
    };
    this.baseState = this.state;
  }

  addModule = () => {
    let newModule = new Modulebo();
    newModule.setID(0);
    newModule.setname(this.state.name);
    newModule.setedvnr(this.state.edvnr);
    newModule.setects(this.state.ects);
    newModule.setworkload(this.state.workload);
    newModule.set_requirement(this.state.requirement);
    newModule.set_outcome(this.state.outcome);
    newModule.set_examtype(this.state.set_examtype);
    newModule.set_instructor(this.state.set_instructor);

    //die Modulepart müssen zur module hinzugefügt werden, entweder durch eine update methode fürs modulpart im backend oder indem die modulepart direkt im spobo hinzugefügt werden
    //let modulIDs=this.state.moduleInSPO.map(module => module.getID());
    //newSPO.setModules(modulIDs);

    API.getAPI()
      .addModule(newModule)
      .then((module) => {
        this.setState(this.baseState);
        this.props.onClose(module); //Aufrufen parent in backend
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
    if (this.props.module) {
      const { module } = this.props;

      this.setState({
        id: module.id,
        name: module.name,
        edvnr: module.edvnr,
        ects: module.ects,
        workload: module.workload,
        requirement: module.requirement,
        outcome: module.outcome,
        examtype: module.examtype,
        instructor: module.instructor,
        //anpassen von id?
      });
    }
  };
  getModulepart = () => {
    const { module } = this.props;
    //TODO: Überprüfen, ob diese Methode wirklich alle Moduleparts aus der DB holt
    API.getAPI().getAllModule().then((response) => {
      if (module) {
        //TODO: anpassen auf die passende Methode in API
        API.getAPI().getAllModulepartForMODULE(module.id).then((modulepart) => {
          //alle moduleparts die in der spo sind aus der response entfernen
          let modulepartOhneModule = response.filter((m) => {
            //Array.some überprüft, ob ein Element in dem Array vorkommt, wenn das Element schon in Module vorhanden ist, wird es dann aus der response rausgefiltert
            return !modulepart.some((m2) => m2.id === m.id);
          });
          this.setState({
            modulepartInModule: modulepart,
            modulepart: modulepartOhneModule,
          });
        });
      }
      else{
        this.setState({
          modulepart: response,
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
    const {module} = this.props;
    if (this.state.activeStep === 0){
      this.getModulepart()
      this.setState({
        activeStep: 1,
      })}
    else if (this.state.activeStep === 1){
    module? this.updateModule() : this.addModule();
    }
    
  };

  //Modulepart hinzufügen Methoden
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
    const newModulepart = this.state.modulepart;
    //alle moduleparts aus this.state.modulepartInModule in newModulepart hinzufügen
    this.state.modulepartInModule.forEach((m) => {
      newModulepart.push(m);
    });
    this.setState({
      checked: [],
      modulepartInModule: [],
      modulepart: newModulepart,
    });
  }
  handleAllRight = () => {
    const newModulepart = this.state.modulepartInModule;
    //alle modulepart aus this.state.modulepart in newModulepart hinzufügen
    this.state.modulepart.forEach((m) => {
      newModulepart.push(m);
    });
    this.setState({
      checked: [],
      modulepart: [],
      modulepartInModule: newModulepart,
    });
  }
  handleCheckedLeft = () => {
    const newModulepart = this.state.modulepart;
    //alle checked modulepart aus this.state.modulepartInmodule in newModulepart hinzufügen
    this.state.modulepartInModule.forEach((m) => {
      if (this.state.checked.includes(m.id)) {
        newModulepart.push(m);
      }
    });

    this.setState({
      checked: [],
      modulepartInModule: newModulepart,
      modulepart: this.state.modulepart.filter((m) => !this.state.checked.includes(m.id)),
    });
  }
  handleCheckedRight = () => {
    const newModulepart = this.state.modulepartInModule;
    //alle checked modulepart aus this.state.modulepart in newModulepart hinzufügen
    this.state.modulepart.forEach((m) => {
      if (this.state.checked.includes(m.id)) {
        newModulepart.push(m);
      }
    });
    this.setState({
      checked: [],
      modulepart: newModulepart,
      modulepartInModule: this.state.modulepartInModule.filter((m) => !this.state.checked.includes(m.id)),
    });
  }

  intersection = (checkedarray, modulepart) => {
    //überprüft ob ein modulpart in dem checkedarray vorhanden ist
    const modulpartIDs = modulepart.map((m) => m.id);
    return checkedarray.filter((c) => modulpartIDs.tabIndexOf(c) !== -1);
  }


renderTextfields(){
  const{name,nameValidationFailed,edvnr,edvnrValidationFailed, ects, ectsValidationFailed, workload, workloadValidationFailed, requirement, requirementValidationFailed, outcome, outcomeValidationFailed, examtype, examtypeValidationFailed, instructor, instructorValidationFailed} = this.state;
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
              label="Modulname"
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
              id="edvnr"
              label="EDVNR"
              variant="outlined"
              value={edvnr}
              onChange={this.numberValueChange}
              error={edvnrValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
              margin="small"
              id="ects"
              label="ECTS"
              variant="outlined"
              value={ects}
              onChange={this.numberValueChange}
              error={ectsValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
              margin="small"
              id="workload"
              label="Arbeitszeit für das Spoelement"
              variant="outlined"
              value={workload}
              onChange={this.textFieldValueChange}
              error={workloadValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              margin="small"
              id="requirement"
              label="Voraussetzung für das Module"
              variant="outlined"
              value={requirement}
              onChange={this.numberValueChange}
              error={requirementValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              margin="small"
              id="outcome"
              label="outcome des Modules"
              variant="outlined"
              value={outcome}
              onChange={this.textFieldValueChange}
              error={outcomeValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              margin="small"
              id="examtype"
              label="examtype"
              variant="outlined"
              value={examtype}
              onChange={this.textFieldValueChange}
              error={examtypeValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              margin="small"
              id="instructor"
              label="instructur"
              variant="outlined"
              value={instructor}
              onChange={this.numberValueChange}
              error={instructorValidationFailed}
            />
          </form>
      </>
    );
  }
  render AddModulepart() {
    const {modulepart, modulepartInModule, checked} = this.state

 //Modulepart, die jeweils auf der linken und rechten Seite ausgewählt sind
 const leftChecked = this.intersection(checked, modulepart);
 const rightChecked = this.intersection(checked, modulepartInModule);

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
           disabled={modulepart.length === 0}
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
           disabled={modulepartInModule.length === 0}
           aria-label="move all left"
         >
           ≪
         </Button>
       </Grid>
     </Grid>
     <Grid item>{customList(modulepartInModule)}</Grid>
   </Grid>
     </>
   );  
}

render() {
    const { show, module } = this.props;
    const {
      
      nameValidationFailed,
      nameEdited,

      edvnrValidationFailed,
      edvnrEdited,

      ectsValidationFailed,
      ectsEdited,

      workloadValidationFailed,
      workloadEdited,

      
      requirementValidationFailed,
      requirementEdited,

      outcomeValidationFailed,
      outcomeEdited,

      examtypeValidationFailed,
      examtypeEdited,

    
      instructorValidationFailed,
      instructorEdited,

      addingInProgress,
      addingError,
      updatingInProgress,
      updatingError,

      activeStep,
    } = this.state;

    let title = "";
    let header = "";

    if (module) {
      // Projekt objekt true, somit ein edit
      title = `Module "${module.name}" bearbeiten`;
      header = "Neue module Daten einfügen";
    } else {
      title = "Erstelle eine neue module";
      header = "module Daten einfügen";
    }

    return show ? (
      <Dialog
        open={show}
        onEnter={this.getInfos}
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
          {activeStep===0? this.renderTextfields():this.renderAddModulpart()}
          <LoadingProgress show={addingInProgress || updatingInProgress} />
          {
            // Show error message in dependency of Projektart prop

         
            // Show error message in dependency of Projektart prop
            module ? (
              <ContextErrorMessage
                error={updatingError}
                contextErrorMsg={`The module ${module.getID()} could not be updated.`}
                onReload={this.updateModule}
              />
            ) : (
              <ContextErrorMessage
                error={addingError}
                contextErrorMsg={`The module could not be added.`}
                onReload={this.addModule}
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
            module ? (
              <Button
                disabled={
                  nameValidationFailed ||
                  edvnrValidationFailed ||
                  ectsValidationFailed ||
                  workloadValidationFailed ||
                  requirementValidationFailed ||
                  outcomeValidationFailed ||
                  examtypeValidationFailed ||
                  instructorValidationFailed
                }
                variant="contained"
                onClick={this.updateModule}
                color="primary"
              >
                {activeStep===0? "Weiter":"Speichern"}  
              </Button>
            ) : (
              <Button
                disabled={
                  nameValidationFailed ||
                  !nameEdited ||
                  edvnrValidationFailed ||
                  !edvnrEdited ||
                  ectsValidationFailed ||
                  !ectsEdited ||
                  workloadValidationFailed ||
                  !workloadEdited ||
                  requirementValidationFailed ||
                  !requirementEdited ||
                  outcomeValidationFailed ||
                  !outcomeEdited ||
                  examtypeValidationFailed ||
                  !examtypeEdited ||
                  instructorValidationFailed ||
                  !instructorEdited
                }
                variant="contained"
                onClick={this.addModule}
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
ModuleForm.propTypes = {
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

export default ModuleForm;
