import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Modulebo from '../../api/BusinessObjects/Modulebo';
import API from '../../api/API';
import {
  Button, IconButton, Dialog, DialogContent, DialogContentText,
   DialogTitle, DialogActions, TextField
} from '@mui/material';
import CloseIcon from '@material-ui/icons/Close';
import ContextErrorMessage from './ContextErrorMessage';
import LoadingProgress from './LoadingProgress';


export class ModuleForm extends Component {
    constructor(props) {
      super(props)
    
      this.state = {

        id:null,
        name:'',
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
        updatingInProgress: false
    };
    this.baseState = this.state;
    }

    addModule = () => {
        let newModule = new Modulebo()
        newModule.setID(0)
        newModule.setname(this.state.name)
        newModule.setedvnr(this.state.edvnr)
        newModule.setects(this.state.ects)
        newModule.setworkload(this.state.workload)
        newModule.set_requirement(this.state.requirement)
        newModule.set_outcome(this.state.outcome)
        newModule.set_examtype(this.state.set_examtype)
        newModule.set_instructor(this.state.set_instructor)

        API.getAPI().addModule(newModule).then(module => {
            this.props.getmodule()
            this.setState(this.baseState);
            this.props.onClose(module); //Aufrufen parent in backend
        }).catch(e =>
            this.setState({
                addingInProgress: false,
                addingError: e
            })
        );
        // Ladeanimation einblenden
        this.setState({
            addingProgress: true,
            addingError: null
        });
    }
// Validierung der Textfeldaenderungen 
textFieldValueChange = (event) => {
  const value = event.target.value;

  let error = false;
  if (value.trim().length === 0) {
      error = true;
  }
  this.setState({
      [event.target.id]: event.target.value,
      [event.target.id + 'ValidationFailed']: error,
      [event.target.id + 'Edited']: true
  });
}

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
      [event.target.id + 'ValidationFailed']: error,
      [event.target.id + 'Edited']: true
  });
}

getInfos = () => {
  if (this.props.module) {
      const {module}=this.props
      
  

      this.setState({
          id: module.id,
          name: module.name,
          edvnr: module.edvnr,
          ects: module.ects,
          workload: module.workload,
          requirement: module.requirement,
          outcome: module.outcome,
          examtype: module.examtype,
          instructor: module.instructor
          //anpassen von id?
      })
  }
}


handleClose = () => {
  this.setState(this.baseState);
  this.props.onClose(null);
}

    render() {
      const { show, module } = this.props;
      const {

          id,
          idValidationFailed,
          idEdited,

          name,
          nameValidationFailed,
          nameEdited,

          edvnr,
          edvnrValidationFailed,
          edvnrEdited,

          ects,
          ectsValidationFailed,
          ectsEdited,

          workload,
          workloadValidationFailed,
          workloadEdited,

          requirement,
          requirementValidationFailed,
          requirementEdited,

          outcome,
          outcomeValidationFailed,
          outcomeEdited,

          examtype,
          examtypeValidationFailed,
          examtypeEdited,

          instructor,
          instructorValidationFailed,
          instructorEdited,

          addingInProgress,
          addingError,
          updatingInProgress,
          updatingError, } = this.state;

      let title = '';
      let header = '';

      if (module) {
          // Projekt objekt true, somit ein edit
          title = `Module "${module.name}" bearbeiten`;
          header = 'Neue module Daten einfügen';
      } else {
          title = 'Erstelle eine neue module';
          header = 'module Daten einfügen';
      }


      return (
          show ?
              <Dialog open={show} onEnter={this.getInfos} onClose={this.handleClose} maxWidth='xs' fullWidth>
                  <DialogTitle>{title}
                      <IconButton onClick={this.handleClose}>
                          <CloseIcon />
                      </IconButton>
                  </DialogTitle>
                  <DialogContent>
                      <DialogContentText>
                          {header}
                      </DialogContentText>

                      <form noValidate autoComplete='off'>

                          <TextField autoFocus type='text' required fullWidth margin='small' id='id' label='id' variant="outlined" value={id}
                              onChange={this.numberFieldValueChange} error={idValidationFailed} />

                          <TextField autoFocus type='text' required fullWidth margin='small' id='name' label='Modulename' variant="outlined" value={name}
                              onChange={this.textFieldValueChange} error={nameValidationFailed} />

                          <TextField type='text' required fullWidth margin='small' id='edvnr' label='EDVNR' variant="outlined" value={edvnr}
                              onChange={this.numberValueChange} error={edvnrValidationFailed} />

                          <TextField  type='text' required fullWidth margin='small' id='ects' label='ECTS' variant="outlined" value={ects}
                              onChange={this.numberValueChange} error={ectsValidationFailed} />


                          <TextField  type='text' required fullWidth margin='small' id='workload' label='Arbeitszeit für das Spoelement' variant="outlined" value={workload}
                              onChange={this.textFieldValueChange} error={workloadValidationFailed} />  

                          <TextField autoFocus type='text' required fullWidth margin='small' id='requirement' label='Voraussetzung für das Module' variant="outlined" value={requirement}
                              onChange={this.numberValueChange} error={requirementValidationFailed} />

                          <TextField  autoFocus type='text' required fullWidth margin='small' id='outcome' label='outcome des Modules' variant="outlined" value={outcome}
                              onChange={this.textFieldValueChange} error={outcomeValidationFailed} />


                          <TextField  autoFocus type='text' required fullWidth margin='small' id='examtype' label='examtype' variant="outlined" value={examtype}
                              onChange={this.textFieldValueChange} error={examtypeValidationFailed} />

                          <TextField  autoFocus type='text' required fullWidth margin='small' id='instructor' label='instructur' variant="outlined" value={instructor}
                              onChange={this.numberValueChange} error={instructorValidationFailed} />

                      </form>
                      <LoadingProgress show={addingInProgress || updatingInProgress} />
                      {
                          // Show error message in dependency of Projektart prop
                          module ?
                              <ContextErrorMessage error={updatingError} contextErrorMsg={`The module ${module.getID()} could not be updated.`} onReload={this.updateModule} />
                              :
                              <ContextErrorMessage error={addingError} contextErrorMsg={`The module could not be added.`} onReload={this.addModule} />
                      }
                  </DialogContent>
                  <DialogActions>
                      <Button onClick={this.handleClose} color='secondary'>
                          Abbrechen
                      </Button>
                      {
                          // If a Projekt is given, show an update button, else an add button
                          module ?
                              <Button disabled={idValidationFailed ||nameValidationFailed || edvnrValidationFailed || ectsValidationFailed || workloadValidationFailed || requirementValidationFailed || outcomeValidationFailed || examtypeValidationFailed || instructorValidationFailed } variant='contained' onClick={this.updateModule} color='primary'>
                                  Speichern
                      </Button>
                              :
                              <Button disabled={idValidationFailed || !idEdited ||nameValidationFailed || !nameEdited || edvnrValidationFailed || !edvnrEdited || ectsValidationFailed || !ectsEdited || workloadValidationFailed || !workloadEdited || requirementValidationFailed || !requirementEdited || outcomeValidationFailed || !outcomeEdited  || examtypeValidationFailed || !examtypeEdited || instructorValidationFailed || !instructorEdited}
                                  variant='contained' onClick={this.addModule} color='primary'>
                                  Hinzufügen
                      </Button>
                      }
                  </DialogActions>
              </Dialog>
              : null
      );
  }
}

export default ModuleForm;
