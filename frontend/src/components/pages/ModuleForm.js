import React, { Component } from 'react';
import Modulebo from '../../api/BusinessObjects/Modulebo';
import API from '../../api/API';
import {
  Button, IconButton, Dialog, DialogContent, DialogContentText,
   DialogTitle, DialogActions, TextField
} from '@mui/material';


export class ModuleForm extends Component {
    constructor(props) {
      super(props)
    
      this.state = {
         
      }
    }
    addModule = () => {
        let newModule = new Modulebo()
        newModule.setID(0)
        newModule.setname(this.state.name)
        newModule.setedvnr
        newModule.set_type(this.state.type)
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
    render() {
      const { show, module } = this.props;
      const {
          name,
          nameValidationFailed,
          nameEdited,

          ects,
          ectsValidationFailed,
          ectsEdited,

          sws,
          swsValidationFailed,
          swsEdited,

          modulepart,
          modulepartValidationFailed,
          modulepartEdited,

          semester,
          semesterValidationFailed,
          semesterEdited,

          studyCourse,
          studyCourseValidationFailed,
          studyCourseEdited,



          addingInProgress,
          addingError,
          updatingInProgress,
          updatingError, } = this.state;

      let title = '';
      let header = '';

      if (module) {
          // Projekt objekt true, somit ein edit
          title = `Module "${module.name}" bearbeiten`;
          header = 'Neue Spo Daten einfügen';
      } else {
          title = 'Erstelle eine neue Spo';
          header = 'Spo Daten einfügen';
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

                          <TextField autoFocus type='text' required fullWidth margin='small' id='name' label='Sponame' variant="outlined" value={name}
                              onChange={this.textFieldValueChange} error={nameValidationFailed} />

                          <TextField type='text' required fullWidth margin='small' id='ects' label='ECTS' variant="outlined" value={ects}
                              onChange={this.numberValueChange} error={ectsValidationFailed} />

                          <TextField  type='text' required fullWidth margin='small' id='sws' label='SWS' variant="outlined" value={sws}
                              onChange={this.numberValueChange} error={swsValidationFailed} />


<TextField  autoFocus type='text' required fullWidth margin='small' id='modulepart' label='Modulteil' variant="outlined" value={modulepart}
                              onChange={this.textFieldValueChange} error={modulepartValidationFailed} />  

<TextField autoFocus type='text' required fullWidth margin='small' id='semester' label='Semester' variant="outlined" value={semester}
                              onChange={this.numberValueChange} error={semesterValidationFailed} />

<TextField  autoFocus type='text' required fullWidth margin='small' id='studyCourse' label='StudyCourse' variant="outlined" value={studyCourse}
                              onChange={this.textFieldValueChange} error={studyCourseValidationFailed} />

                      </form>
                      <LoadingProgress show={addingInProgress || updatingInProgress} />
                      {
                          // Show error message in dependency of Projektart prop
                          module ?
                              <ContextErrorMessage error={updatingError} contextErrorMsg={`The Spo ${module.getID()} could not be updated.`} onReload={this.updateModule} />
                              :
                              <ContextErrorMessage error={addingError} contextErrorMsg={`The Spo could not be added.`} onReload={this.addModule} />
                      }
                  </DialogContent>
                  <DialogActions>
                      <Button onClick={this.handleClose} color='secondary'>
                          Abbrechen
                      </Button>
                      {
                          // If a Projekt is given, show an update button, else an add button
                          module ?
                              <Button disabled={nameValidationFailed || ectsValidationFailed || swsValidationFailed || modulepartValidationFailed || semesterValidationFailed || studyCourseValidationFailed  } variant='contained' onClick={this.updateModule} color='primary'>
                                  Speichern
                      </Button>
                              :
                              <Button disabled={nameValidationFailed || !nameEdited || ectsValidationFailed || !ectsEdited || swsValidationFailed || !swsEdited || modulepartValidationFailed || !modulepartEdited || semesterValidationFailed || !semesterEdited || studyCourseValidationFailed || !studyCourseEdited}
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
