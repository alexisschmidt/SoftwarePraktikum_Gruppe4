import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { withStyles } from '@material-ui/core';

import Box from '@mui/material/Box';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import ModuleForm from './pages/ModuleForm';
import ModulepartForm from './pages/ModulepartForm';
import SpoForm from './pages/SpoForm';

import API from '../api/API';
import { Button } from '@mui/material';


class AdminSpoAnsicht extends Component {

    constructor(props) {
        super(props);

        this.state = {
            spo: null,
            studycourses: [],
			modules: [],
			moduleparts: [],
			semester: [],
            loadingProgress: false,
            error: null,

            
            spoFormIsOpen: false,
            moduleFormOpen: false,
            modulepartFormOpen: false,
            selectedSPO:null,
            selectedModule:null, 
            selectedModulepart:null,
            // müssen die zwei auch sein oder nur selectedspo?
            
            spoId: null,
            studyCourseId: null


        };
    }

 

    getAllStudycoursesById = () => {
        const id = this.props.match.params.id;
        API.getAPI().getAllStudycoursesById(id).then(studyCoursebo => {            
            this.setState({
                studycourses: studyCoursebo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                studycourses: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    getUser = (hash) => {
        API.getAPI().getUser(hash).then(userbo => {            
            this.setState({
                user: userbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                user: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    getPerson = (hash) => {
        API.getAPI().getPerson(hash).then(personbo => {            
            this.setState({
                person: personbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                person: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    sortModuleBySemster () {

        const sorted = [...this.state.spo.modules].sort((el, last) => el?.moduleparts[0].semester < last?.moduleparts[0].semester);
        this.setState({
            spo: {...this.state.spo, modules: sorted}
        });
    }

	getAllModulesBySpoId = (id) => {

        const api = API.getAPI();
        
        api.getSpoById(id).then(spo => {

            this.setState({
                spo: {...spo, modules: []},
                loadingProgress: false,
                error: null
            }, () => {
                spo.modules.forEach(moudleHash => {
                    api.getModuleByHash(moudleHash).then(m => {                
    
                        api.getModulePartByHash(moudleHash).then(modulePart => {
                            
                            if (m && m.length) {
                                let newModule = m[0];
                                newModule.moduleparts = modulePart;
    
                                this.setState({
                                    spo: { ...this.state.spo, modules: [...this.state.spo.modules, newModule] }
                                });
                            } else {
                                this.setState({
                                    spo: { ...this.state.spo, modules: [...m] }
                                });
    
                            }
                        });                    
                    });
                });
            });
        });

        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    CreateStudycoursesFormClosed = event => {
        this.setState({
            showCreateStudycoursesForm: false,
        })
    }

    buttonNavigateToCourseClicked(id) {
        this.props.history.push(`/admin/${id}`);
    }


    getSemsterFromModule(element) {
        if (element) {
            if (element.moduleparts && element.moduleparts.length >= 1) {
                return `${element.moduleparts[0].semester}`;
            }
        } 
        return '1'
    }
    

    componentDidMount() {
        const studyCourseId = this.props.match.params.studyCourseID;
        const spoId = this.props.match.params.spoID;
        
        this.setState({
            studyCourseId: studyCourseId,
            spoId: spoId
        });
        
        this.getAllModulesBySpoId(spoId);

        // this.getAllModulesBySpoId(spoId);
        
        /*
        this.getAllStudycoursesById();
        this.getAllModulesById();
        this.getAllModulePartsById();
        this.getAllSemesterById();
        this.getAllPersonsById();
        this.getAllSposById();
        this.getAllUsersById();
        */
    }

    handleSpoEdit = () => {
        this.setState({
            spoFormIsOpen:true,
            selectedSPO:this.state.spo,
        })
    }
    handleModuleEdit = (moduleElement) => {
        this.setState({
            moduleFormOpen:true,
            selectedModule:moduleElement,
        })
    }
    handleModulePartEdit = (modulePartElement) => {
        this.setState({
            modulepartFormOpen:true,
            selectedModulepart:modulePartElement,
        })
    }

    handleGoToEdit = () => {
        this.props.history.push(`/admin/${this.state.studyCourseId}/${this.state.spoId}/edit`);
    }

    handleGoToNoneEdit = () => {
        this.props.history.push(`/admin/${this.state.studyCourseId}/${this.state.spoId}`);
    }


    spoFormClosed = (event) => {
        this.setState({
          spoFormIsOpen: false,
          selectedSPO:null,
        });
      };
      moduleFormClosed = (event) => {
        this.setState({
          moduleFormOpen: false,
          selectedModule:null,
        });
      };
      modulepartFormClosed = (event) => {
        this.setState({
          modulepartFormOpen: false,
          selectedModulepart: null,
        });
      };

    render() {
        const { classes, bearbeitenBoolean } = this.props;
        const { loadingProgress, error, studycourses, modules, moduleparts, semester, person, spo, user, spoFormIsOpen, moduleFormOpen, modulepartFormOpen, selectedSPO, selectedModule, selectedModulepart} = this.state;
        return (
            <>
                        <Box sx={{ width: '100%', maxWidth: 650, marginLeft: 'auto', marginRight: 'auto' }} className="admin-spo-container">
            <div>
                <Card>
                    <CardContent>

                        <div className="admin-spo-box fix-header-box">
                            
                            <div className="admin-spo-box-semster">
                                Semester
                            </div>

                            <div className="admin-spo-box-edv">
                                EDV-Nr.
                            </div>

                            <div className="admin-spo-box-module">
                                Modul (Kursbezeichnung)
                            </div>

                            <div className="admin-spo-box-sws">
                                SWS
                            </div>

                            <div className="admin-spo-box-ects">
                                ECTS
                            </div>

                            <div className="admin-spo-box-pruefung">
                                Prüfung
                            </div> 
                        </div>

                        {
                            spo?.modules?.map((moduleElement) => {
                                return (
                                    <>
                                    <Accordion>
                                    <AccordionSummary
                                        expandIcon={<ExpandMoreIcon />}
                                        aria-controls="panel1a-content"
                                        id="panel1a-header"
                                        >
                                    <div className="admin-spo-box fix-header-box">

                                        <div className="admin-spo-box-semster">
                                            {/* TODO ALexis. Wenn backend ready, erstze alle static daten mit den aus der dantenbank. module sollte das modul object sein"! */}
                                            {/* {moduleElement.id} */}
                                            {this.getSemsterFromModule(moduleElement)}
                                        </div>

                                        <div className="admin-spo-box-edv">
                                            {moduleElement.edvnr}
                                        </div>

                                        <div className="admin-spo-box-module">
                                            {moduleElement.name}
                                        </div>

                                        <div className="admin-spo-box-sws">
                                            
                                        </div>

                                        <div className="admin-spo-box-ects">
                                            {moduleElement.ects}
                                        </div>

                                        <div className="admin-spo-box-pruefung">
                                        	{moduleElement.examtype}              
                                        </div>                                        

                                    </div>
                                    </AccordionSummary>
                                                    <AccordionDetails>
                                                        <table cellPadding="8">
                                                            <tbody>
                                                            <tr>
                                                            <td>Title</td>
                                                            <td>{moduleElement.title}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Language</td>
                                                            <td>{moduleElement.outcome}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Literature</td>
                                                            <td>{moduleElement.requirement}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Sources</td>
                                                            <td>{moduleElement.type}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Connection</td>
                                                            <td>{moduleElement.workload}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Instructor</td>
                                                            <td>{moduleElement.instructor}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Createdby</td>
                                                            <td>{moduleElement.createdby}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Creationdate</td>
                                                            <td>{moduleElement.creationdate}</td>
                                                            </tr>
                                                            </tbody>
                                                        </table>
                                                        {
                                                            bearbeitenBoolean?
                                                            <div className=''>
                                                            <Button onClick={()=>this.handleModuleEdit(moduleElement)}> Modul bearbeiten</Button>
                                                            </div>
                                                            :null
                                                        }
                                                    </AccordionDetails>
                                                </Accordion>
                                    
                                    {
                                        moduleElement?.moduleparts?.map((modulePartElement) => {
                                
                                            return (
                                                <Accordion>
                                                    <AccordionSummary
                                                        expandIcon={<ExpandMoreIcon />}
                                                        aria-controls="panel1a-content"
                                                        id="panel1a-header"
                                                    >
                                                        <div className="admin-spo-accord-box">

                                                            <div className="admin-spo-accord-box-semster">
                                                                {modulePartElement.semester}
                                                            </div>

                                                            <div className="admin-spo-box-edv">
                                                                {/* TODO ALexis. Wenn backend ready, erstze alle static daten mit den aus der dantenbank. modulePartElement sollte das part modul object sein"! */}
                                                                {modulePartElement.edvnr}
                                                            </div>

                                                            <div className="admin-spo-accord-box-module">
                                                                {modulePartElement.name}
                                                            </div>

                                                            <div className="admin-spo-accord-box-sws">
                                                                {modulePartElement.sws}
                                                            </div>

                                                            <div className="admin-spo-accord-box-ects">
                                                                {modulePartElement.ects}
                                                            </div>
                                                        </div>
                                                    </AccordionSummary>
                                                    <AccordionDetails>
                                                        <table cellPadding="8">
                                                            <tbody>
                                                            <tr>
                                                            <td>Language</td>
                                                            <td>{modulePartElement.language}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Literature</td>
                                                            <td>{modulePartElement.literature}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Sources</td>
                                                            <td>{modulePartElement.sources}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Connection</td>
                                                            <td>{modulePartElement.connection}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Description</td>
                                                            <td>{modulePartElement.description}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Workload</td>
                                                            <td>{modulePartElement.workload}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Professor</td>
                                                            <td>{modulePartElement.professor}</td>
                                                            </tr>
                                                            <tr>
                                                            <td>Creationdate</td>
                                                            <td>{modulePartElement.creationdate}</td>
                                                            </tr>
                                                            </tbody>
                                                        </table>

                                                            {
                                                                bearbeitenBoolean?
                                                                <div className=''>
                                                                <Button onClick={() => this.handleModulePartEdit(modulePartElement)}> Modulpart bearbeiten</Button>
                                                                </div>
                                                                :null
                                                            }
                                                    </AccordionDetails>
                                                </Accordion>
                                            )
                                        })
                                    }
                                    </>
                                )
                            })
                        }

                            {
                                bearbeitenBoolean?
                                <div className='button-spo-edit-container'>
                                    <Button onClick={this.handleGoToNoneEdit}>  Bearbeitungs Modus Verlassen </Button>
                                    <Button onClick={this.handleSpoEdit}> SPO bearbeiten</Button>
                                </div>
                                :
                                <div className='button-spo-edit-container'>
                                    <Button onClick={this.handleGoToEdit}> Zum Bearbeitungs Modus</Button>
                                </div>
                            }
                    </CardContent>
                </Card>
            </div>
        </Box>
        {bearbeitenBoolean?<>
            {selectedSPO?<SpoForm show={spoFormIsOpen} spo={selectedSPO} onClose={this.spoFormClosed} />:null}
            {selectedModule?<ModuleForm show={moduleFormOpen} module ={selectedModule} onClose={this.moduleFormClosed} />:null}
            {selectedModulepart?<ModulepartForm show={modulepartFormOpen} modulepart={selectedModulepart} onClose={this.modulepartFormClosed} />:null}
              </>
              :null}
              </>
        )
    }


}
/** Component specific styles */
const styles = theme => ({
    root: {
        width: '100%',
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(2),
    },
    content: {
        margin: theme.spacing(1),
    },
    table: {
        minWidth: 700,
    },
    header:{
        marginBottom: theme.spacing(1),
        paddingLeft: theme.spacing(1),
        paddingRight: theme.spacing(1),
    },
    button:{
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(3),
        float: 'right'
    }
});

/** PropTypes */
AdminSpoAnsicht.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    /** @ignore */
    location: PropTypes.object.isRequired,
   
}


export default withRouter(withStyles(styles)(AdminSpoAnsicht));