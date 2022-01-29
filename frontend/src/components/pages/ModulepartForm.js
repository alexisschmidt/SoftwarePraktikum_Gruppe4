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
  MenuItem,
  Grid,
  
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
    newModulepart.setsws(this.state.sws);
    newModulepart.setlanguage(this.state.language);
    newModulepart.setdescription(this.state.description);
    newModulepart.setconnection(this.state.connection);
    newModulepart.setliterature(this.state.literature);
    newModulepart.setsources(this.state.sources);
    newModulepart.setsemester(this.state.semester);
    newModulepart.setprofessor(this.state.professor);

    

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
      <Dialog open={show} onClose={this.handleClose} maxWidth="lg" fullWidth>
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
              label="Modulteilname"
              variant="outlined"
              value={name}
              onChange={this.textFieldValueChange}
              error={nameValidationFailed}
            />

            {/* <TextField
              type="text"
              required
              fullWidth
              id="description"
              label="Bezeichnung"
              variant="outlined"
              value={description}
              onChange={this.textFieldValueChange}
              error={descriptionValidationFailed}
            /> */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Bezeichnung des Modulteils" fullWidth select value={description?description:""} onChange={(e) => this.setState({description_id:e.target.value})}>
                        {description?description.map(s => <MenuItem key={s.id} value={s.id}>{s.description}</MenuItem>):<MenuItem value="">Keine Bezeichnung vorhanden</MenuItem>}
                    </TextField>
                </Grid>

            {/* <TextField
              type="text"
              required
              fullWidth
              id="edvnr"
              label="EDVNR"
              variant="outlined"
              value={edvnr}
              onChange={this.numberValueChange}
              error={edvnrValidationFailed}
            /> */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="EDV-Nr" fullWidth select value={edvnr?edvnr:""} onChange={(e) => this.setState({edvnr_id:e.target.value})}>
                        {edvnr?edvnr.map(s => <MenuItem key={s.id} value={s.id}>{s.edvnr}</MenuItem>):<MenuItem value="">Keine EDV-NR. vorhanden</MenuItem>}
                    </TextField>
                </Grid>

            {/* <TextField
              type="text"
              required
              fullWidth
              id="ects"
              label="ECTS"
              variant="outlined"
              value={ects}
              onChange={this.numberValueChange}
              error={ectsValidationFailed}
            /> */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="ECTS Punkte" fullWidth select value={ects?ects:""} onChange={(e) => this.setState({ects_id:e.target.value})}>
                        {ects?ects.map(s => <MenuItem key={s.id} value={s.id}>{s.ects}</MenuItem>):<MenuItem value="">Keine ECTS Punkte vorhanden</MenuItem>}
                    </TextField>
                </Grid>

           {/*  <TextField
              type="text"
              required
              fullWidth
              id="workload"
              label="Arbeitszeit für das Spoelement"
              variant="outlined"
              value={workload}
              onChange={this.textFieldValueChange}
              error={workloadValidationFailed}
            /> */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Arbeitsaufwand" fullWidth select value={workload?workload:""} onChange={(e) => this.setState({workload_id:e.target.value})}>
                        {workload?workload.map(s => <MenuItem key={s.id} value={s.id}>{s.workload}</MenuItem>):<MenuItem value="">Keine Daten für Arbeitsaufwand vorhanden</MenuItem>}
                    </TextField>
                </Grid>

           {/*  <TextField
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
            /> */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Semesterwochenstunden(SWS)zeitliche Umfang" fullWidth select value={sws?sws:""} onChange={(e) => this.setState({sws_id:e.target.value})}>
                        {sws?sws.map(s => <MenuItem key={s.id} value={s.id}>{s.sws}</MenuItem>):<MenuItem value="">Keine Semesterwochenstunden(SWS) vorhanden</MenuItem>}
                    </TextField>
                </Grid>

           {/*  <TextField
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
 */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Sprache" fullWidth select value={language?language:""} onChange={(e) => this.setState({language_id:e.target.value})}>
                        {language?language.map(s => <MenuItem key={s.id} value={s.id}>{s.language}</MenuItem>):<MenuItem value="">Keine Sprache zur auswahl vorhanden</MenuItem>}
                    </TextField>
                </Grid>

            {/* <TextField
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
            /> */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Verbindung zu anderen Modulteilen" fullWidth select value={connection?connection:""} onChange={(e) => this.setState({connection_id:e.target.value})}>
                        {connection?connection.map(s => <MenuItem key={s.id} value={s.id}>{s.connection}</MenuItem>):<MenuItem value="">Keine möfliche Verbindung vorhanden</MenuItem>}
                    </TextField>
                </Grid>

           {/*  <TextField
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

 */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Literatur für das Modulteil" fullWidth select value={literature?literature:""} onChange={(e) => this.setState({literature_id:e.target.value})}>
                        {literature?literature.map(s => <MenuItem key={s.id} value={s.id}>{s.literature}</MenuItem>):<MenuItem value="">Keine literature vorhanden</MenuItem>}
                    </TextField>
                </Grid>

           {/*  <TextField
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
 */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Quellen" fullWidth select value={sources?sources:""} onChange={(e) => this.setState({sources_id:e.target.value})}>
                        {sources?sources.map(s => <MenuItem key={s.id} value={s.id}>{s.sources}</MenuItem>):<MenuItem value="">Keine Quellen vorhanden</MenuItem>}
                    </TextField>
                </Grid>

           {/*  <TextField
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
            /> */}

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Semester" fullWidth select value={semester?semester:""} onChange={(e) => this.setState({semester_id:e.target.value})}>
                        {semester?semester.map(s => <MenuItem key={s.id} value={s.id}>{s.semester}</MenuItem>):<MenuItem value="">Keine Semester zur auswahl vorhanden</MenuItem>}
                    </TextField>
                </Grid>

            {/* <TextField
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
            */}
          

<Grid item xs={12} sm={8} md={8}>
                    <TextField label="Professor" fullWidth select value={professor?professor:""} onChange={(e) => this.setState({professor_id:e.target.value})}>
                        {professor?professor.map(s => <MenuItem key={s.id} value={s.id}>{s.professor}</MenuItem>):<MenuItem value="">Keine Professor zur auswahl vorhanden</MenuItem>}
                    </TextField>
                </Grid> 
                
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
