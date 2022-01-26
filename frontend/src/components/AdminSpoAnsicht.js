import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import { withStyles } from '@material-ui/core';

import Box from '@mui/material/Box';
import Accordion from '@mui/material/Accordion';
import AccordionSummary from '@mui/material/AccordionSummary';
import AccordionDetails from '@mui/material/AccordionDetails';
import Typography from '@mui/material/Typography';
import ExpandMoreIcon from '@mui/icons-material/ExpandMore';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';


import API from '../api/API';



class AdminSpoAnsicht extends Component {

    constructor(props) {
        super(props);

        this.state = {
            studycourses: [],
			modules: [
                {
                    id: 1,
                    moduleparts:[]
                },
                {
                    id: 2,
                    moduleparts:[
                        {
                            id: 2345
                        },
                        {
                            id: 123
                        },
                        {
                            id: 222
                        }
                    ]
                },
                {
                    id: 3,
                    moduleparts:[
                        {
                            id: 8
                        }
                    ]
                },
                {
                    id: 4,
                    moduleparts:[]
                }
            ],
			moduleparts: [],
			semester: [],
            loadingProgress: false,
            error: null,
            //showStudiengangAnlegenForm: false

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

	getAllModulesById = () => {
        API.getAPI().getAllModulesById().then(modulebo => {            
            this.setState({
                modules: modulebo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                modules: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

	getAllModulePartsById = () => {
        API.getAPI().getAllModulePartsById().then(modulepartbo => {            
            this.setState({
                moduleparts: modulepartbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                moduleparts: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

	getAllSemesterById = () => {
        API.getAPI().getAllSemesterById().then(semesterbo => {            
            this.setState({
                semester: semesterbo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                semester: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }


    getAllPersonsById = () => {
        API.getAPI().getAllPersonsById().then(personbo => {            
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

    getAllSposById = () => {
        API.getAPI().getAllSposById().then(spobo => {            
            this.setState({
                spo: spobo,
                loadingProgress: false,
                error: null
            });
        }).catch(e => {
            this.setState({
                semester: [],
                loadingProgress: false,
                error: e
            });
        });
        
        this.setState({
            loadingProgress: true,
            error: null
        });
    }

    getAllUsersById = () => {
        API.getAPI().getAllUsersById().then(userbo => {            
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

    CreateStudycoursesFormClosed = event => {
        this.setState({
            showCreateStudycoursesForm: false,
        })
    }

    buttonNavigateToCourseClicked(id) {
        this.props.history.push(`/admin/${id}`);
    }

    componentDidMount() {
        const studyCourseId = this.props.match.params.studyCourseID;
        const spoId = this.props.match.params.spoID;
        
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

    render() {
        const { classes } = this.props;
        const { loadingProgress, error, studycourses, modules, moduleparts, semester, person, spo, user} = this.state;
        return (
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
                            modules.map((moduleElement) => {
                                return (
                                    <>
                                    <div className="admin-spo-box fix-header-box">

                                        <div className="admin-spo-box-semster">
                                            {/* TODO ALexis. Wenn backend ready, erstze alle static daten mit den aus der dantenbank. module sollte das modul object sein"! */}
                                            {moduleElement.id}
                                        </div>

                                        <div className="admin-spo-box-edv">
                                            VS: 3350
                                        </div>

                                        <div className="admin-spo-box-module">
                                            Einstuifungs englisch
                                        </div>

                                        <div className="admin-spo-box-sws">
                                            0
                                        </div>

                                        <div className="admin-spo-box-ects">
                                            0
                                        </div>

                                        <div className="admin-spo-box-pruefung">
                                            VS:LU
                                        </div>

                                    </div>
                                    
                                    {
                                        moduleElement.moduleparts.map((modulePartElement) => {
                                
                                            return (
                                                <Accordion>
                                                    <AccordionSummary
                                                        expandIcon={<ExpandMoreIcon />}
                                                        aria-controls="panel1a-content"
                                                        id="panel1a-header"
                                                    >
                                                        <div className="admin-spo-accord-box">

                                                            <div className="admin-spo-accord-box-semster">
                                                            </div>

                                                            <div className="admin-spo-box-edv">
                                                                {/* TODO ALexis. Wenn backend ready, erstze alle static daten mit den aus der dantenbank. modulePartElement sollte das part modul object sein"! */}
                                                                {modulePartElement.id}
                                                            </div>

                                                            <div className="admin-spo-accord-box-module">
                                                                Was auch immer
                                                            </div>

                                                            <div className="admin-spo-accord-box-sws">
                                                                0
                                                            </div>

                                                            <div className="admin-spo-accord-box-ects">
                                                                0
                                                            </div>

                                                            <div className="admin-spo-accord-box-pruefung">
                                                            </div>

                                                        </div>
                                                    </AccordionSummary>
                                                    <AccordionDetails>
                                                        <Typography>
                                                            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse
                                                            malesuada lacus ex, sit amet blandit leo lobortis eget.
                                                        </Typography>
                                                    </AccordionDetails>
                                                </Accordion>
                                            )
                                        })
                                    }
                                    </>
                                )
                            })
                        }
                    </CardContent>
                </Card>
            </div>
        </Box>
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