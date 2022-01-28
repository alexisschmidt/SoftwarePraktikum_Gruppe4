import React, { Component } from "react";
import Modulepartbo from "../../api/BusinessObjects/Modulepartbo";
import API from "../../api/API";
import {
  Button,
  IconButton,
  Dialog,
  DialogContent,
  DialogContentText,
  DialogTitle,
  DialogActions,
  TextField,
  Box,
  MenuItem,
} from "@mui/material";

import CloseIcon from "@material-ui/icons/Close";
import ContextErrorMessage from "../dialogs/ContextErrorMessage";
import LoadingProgress from "../dialogs/LoadingProgress";

export class ModulepartForm extends Component {
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

      sws: null,
      swsValidationFailed: false,
      swsEdited: false,

      language: null,
      languageValidationFailed: false,
      languageEdited: false,

      description: null,
      descriptionValidationFailed: false,
      descriptionEdited: false,

      connection: null,
      connectionValidationFailed: false,
      connectionEdited: false,

      literature: null,
      literatureValidationFailed: false,
      literatureEdited: false,

      sources: null,
      sourcesValidationFailed: false,
      sourcesEdited: false,

      semester: null,
      semesterValidationFailed: false,
      semesterEdited: false,

      professor: null,
      professorValidationFailed: false,
      professorEdited: false,

      addingError: null,
      addingInProgress: false,

      updatingError: null,
      updatingInProgress: false,
    };
    this.baseState = this.state;
  }
  componentDidMount = () => {
    this.getInfos();
  };

  addModulepart = () => {
    let newModulepart = new Modulepartbo();
    newModulepart.setID(0);
    newModulepart.setname(this.state.name);
    newModulepart.setedvnr(this.state.edvnr);
    newModulepart.setects(this.state.ects);
    newModulepart.setworkload(this.state.workload);
    newModulepart.set_sws(this.state.sws);
    newModulepart.set_language(this.state.language);
    newModulepart.set_description(this.state.description);
    newModulepart.set_connection(this.state.connection);
    newModulepart.set_literature(this.state.literature);
    newModulepart.set_sources(this.state.sources);
    newModulepart.set_semester(this.state.semester);
    newModulepart.set_professor(this.state.professor);

    API.getAPI()
      .addModuleParts(newModulepart)
      .then((modulepart) => {
        this.props.getmodulepart();
        this.setState(this.baseState);
        this.props.onClose(modulepart); //Aufrufen parent in backend
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
    if (this.props.modulepart) {
      const { modulepart } = this.props;

      this.setState({
        id: modulepart.id,
        name: modulepart.name,
        edvnr: modulepart.edvnr,
        ects: modulepart.ects,
        workload: modulepart.workload,
        sws: modulepart.sws,
        language: modulepart.language,
        description: modulepart.description,
        connection: modulepart.connection,
        literature: modulepart.literature,
        sources: modulepart.sources,
        semester: modulepart.semester,
        professor: modulepart.professor,
        //anpassen von id?
      });
    }
  };

  handleClose = () => {
    this.setState(this.baseState);
    this.props.onClose(null);
  };

  render() {
    const { show, modulepart } = this.props;
    const {
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

      sws,
      swsValidationFailed,
      swsEdited,

      language,
      languageValidationFailed,
      languageEdited,

      description,
      descriptionValidationFailed,
      descriptionEdited,

      connection,
      connectionValidationFailed,
      connectionEdited,

      literature,
      literatureValidationFailed,
      literatureEdited,

      sources,
      sourcesValidationFailed,
      sourcesEdited,

      semester,
      semesterValidationFailed,
      semesterEdited,

      professor,
      professorValidationFailed,
      professorEdited,

      addingInProgress,
      addingError,
      updatingInProgress,
      updatingError,
    } = this.state;

    let title = "";
    let header = "";

    if (modulepart) {
      // Projekt objekt true, somit ein edit
      title = `Modulepart "${modulepart.name}" bearbeiten`;
      header = "Neue modulepart Daten einfügen";
    } else {
      title = "Erstelle eine neue modulepart";
      header = "modulepart Daten einfügen";
    }

    return show ? (
      <Dialog open={show} onClose={this.handleClose} maxWidth="xs" fullWidth>
        <DialogTitle>
          {title}
          <IconButton onClick={this.handleClose}>
            <CloseIcon />
          </IconButton>
        </DialogTitle>
        <DialogContent>
          <DialogContentText>{header}</DialogContentText>

          <form noValidate autoComplete="off">
            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              id="name"
              label="Modulename"
              variant="outlined"
              value={name}
              onChange={this.textFieldValueChange}
              error={nameValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
              id="description"
              label="description"
              variant="outlined"
              value={ects}
              onChange={this.textFieldValueChange}
              error={descriptionValidationFailed}
            />

            <TextField
              type="text"
              required
              fullWidth
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
              id="sws"
              label="sws"
              variant="outlined"
              value={sws}
              onChange={this.numberValueChange}
              error={swsValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              id="language"
              label="language des Modules"
              variant="outlined"
              value={language}
              onChange={this.textFieldValueChange}
              error={languageValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              id="connection"
              label="connection"
              variant="outlined"
              value={connection}
              onChange={this.textFieldValueChange}
              error={connectionValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              id="literature"
              label="literature"
              variant="outlined"
              value={literature}
              onChange={this.textFieldValueChange}
              error={literatureValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              id="sources"
              label="sources"
              variant="outlined"
              value={sources}
              onChange={this.textFieldValueChange}
              error={sourcesValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              id="semester"
              label="semester"
              variant="outlined"
              value={semester}
              onChange={this.numberValueChange}
              error={semesterValidationFailed}
            />

            <TextField
              autoFocus
              type="text"
              required
              fullWidth
              id="professor"
              label="professor"
              variant="outlined"
              value={professor}
              onChange={this.textFieldValueChange}
              error={professorValidationFailed}
            />
          </form>
          <LoadingProgress show={addingInProgress || updatingInProgress} />
          {
            // Show error message in dependency of Projektart prop
            modulepart ? (
              <ContextErrorMessage
                error={updatingError}
                contextErrorMsg={`The modulepart ${modulepart.getID()} could not be updated.`}
                onReload={this.updateModulepart}
              />
            ) : (
              <ContextErrorMessage
                error={addingError}
                contextErrorMsg={`The modulepart could not be added.`}
                onReload={this.addModulepart}
              />
            )
          }
        </DialogContent>
        <DialogActions>
          <Button onClick={this.handleClose} color="secondary">
            Abbrechen
          </Button>
          {
            // If a Projekt is given, show an update button, else an add button
            modulepart ? (
              <Button
                disabled={
                  nameValidationFailed ||
                  edvnrValidationFailed ||
                  ectsValidationFailed ||
                  workloadValidationFailed ||
                  swsValidationFailed ||
                  languageValidationFailed ||
                  descriptionValidationFailed ||
                  connectionValidationFailed ||
                  literatureValidationFailed ||
                  sourcesValidationFailed ||
                  semesterValidationFailed ||
                  professorValidationFailed
                }
                variant="contained"
                onClick={this.updateModulepart}
                color="primary"
              >
                Speichern
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
                  swsValidationFailed ||
                  !swsEdited ||
                  languageValidationFailed ||
                  !languageEdited ||
                  descriptionValidationFailed ||
                  !descriptionEdited ||
                  connectionValidationFailed ||
                  !connectionEdited ||
                  literatureValidationFailed ||
                  !literatureEdited ||
                  sourcesValidationFailed ||
                  !sourcesEdited ||
                  semesterValidationFailed ||
                  !semesterEdited ||
                  professorValidationFailed ||
                  !professorEdited
                }
                variant="contained"
                onClick={this.addModulepart}
                color="primary"
              >
                Hinzufügen
              </Button>
            )
          }
        </DialogActions>
      </Dialog>
    ) : null;
  }
}

export default ModulepartForm;
