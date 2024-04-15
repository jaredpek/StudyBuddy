
import "./StudyAreasPage.css";
import Layout from "../../components/layout/Layout";
import { useEffect, useState } from "react";
import axios from "axios";
import useIsAuthenticated from 'react-auth-kit/hooks/useIsAuthenticated';
import StudyArea from "../../components/study_areas/StudyArea";
import Title from "../../components/layout/Title";

/**
 * Study areas page that displays available study areas for users to book
 * @returns {JSX.Element} The rendered StudyAreasPage element
 */
const StudyAreasPage = () => {
    const [areas, setAreas] = useState([]);
    const [coord, setCoord] = useState({lat: -1, lng: -1});
    const isAuthenticated = useIsAuthenticated();

    useEffect(() => {
        navigator.geolocation.getCurrentPosition(
            (pos) => setCoord({lat: pos.coords.latitude, lng: pos.coords.longitude}),
            () => setCoord({lat: false, lng: false}), 
            {enableHighAccuracy: true}
        )
    }, [])

    useEffect(() => {
        const {lat, lng} = coord;
        if (lat === -1 || lng === -1) return;
        axios.get(`${import.meta.env.VITE_BACKEND_URL}/api/study_areas/${(lat && lng) ? `?lat=${lat}&lng=${lng}` : ""}`)
        .then(({data: {study_areas}}) => setAreas(study_areas))
    }, [coord])

    return (
        <Layout current="study_areas">
            <Title title="Study Areas" />
            {!isAuthenticated && <div style={{marginBottom: 15}}>Please login to book a slot at a study area!</div>}
            <div style={{display: "grid", gap: 10}}>
                { areas.map(area => <StudyArea key={area.id} area={area} authed={isAuthenticated} />) }
            </div>
        </Layout>
    );
};
export default StudyAreasPage;