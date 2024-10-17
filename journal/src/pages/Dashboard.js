import React, { useState } from "react";
import JournalInput from "../components/JournalInput";
import EmotionTrackBar from "../components/EmotionTrackBar";
import EmotionGraph from "../components/EmotionGraph";
import ExercisePanel from "../components/ExercisePanel";
import NavBar from "../components/NavBar";
import EmotionLineChart from "../components/EmotionLineChart";
// import EmotionWordCloud from "../components/EmotionWordCloud";
import axios from "axios";

const Dashboard = () => {
  const [journal, setJournal] = useState("");
  const [loadingSubmit, setLoadingSubmit] = useState(false);
  const [loadingExercise, setLoadingExercise] = useState(false);

  const [emotionLevels, setEmotionLevels] = useState({
    happy: 0,
    sad: 0,
    angry: 0,
    anxious: 0,
    confused: 0,
  });

  const sampleWords = [
    { text: "happy", value: 20 },
    { text: "sad", value: 10 },
    { text: "anxious", value: 15 },
    { text: "love", value: 25 },
    { text: "fear", value: 5 },
  ];

  const [wordCloudData, setWordCloudData] = useState(sampleWords);

  const sampleData = [
    {
      date: "2024-09-01",
      happy: 70,
      sad: 30,
      angry: 20,
      anxious: 50,
      confused: 10,
    },
    {
      date: "2024-09-02",
      happy: 60,
      sad: 40,
      angry: 10,
      anxious: 30,
      confused: 50,
    },
    {
      date: "2024-09-03",
      happy: 60,
      sad: 20,
      angry: 10,
      anxious: 20,
      confused: 5,
    },
    {
      date: "2024-09-04",
      happy: 20,
      sad: 70,
      angry: 20,
      anxious: 30,
      confused: 10,
    },
    {
      date: "2024-09-05",
      happy: 15,
      sad: 5,
      angry: 15,
      anxious: 35,
      confused: 45,
    },
    {
      date: "2024-09-06",
      happy: 60,
      sad: 40,
      angry: 10,
      anxious: 30,
      confused: 50,
    },
    {
      date: "2024-09-07",
      happy: 25,
      sad: 10,
      angry: 50,
      anxious: 20,
      confused: 10,
    },
    {
      date: "2024-09-08",
      happy: 10,
      sad: 20,
      angry: 10,
      anxious: 35,
      confused: 10,
    },
    {
      date: "2024-09-10",
      happy: 15,
      sad: 25,
      angry: 20,
      anxious: 30,
      confused: 50,
    },
    {
      date: "2024-09-11",
      happy: 45,
      sad: 45,
      angry: 20,
      anxious: 35,
      confused: 35,
    },
    // Add more data as needed
  ];

  const [exerciseSuggestion, setExerciseSuggestion] = useState("");
  const [lineChartData, setLineChartData] = useState(sampleData);

  // Handle journal input changes
  const handleJournalChange = (event) => {
    setJournal(event.target.value);
  };

  // Map emotions from backend response to track bar values
  const mapEmotionsToLevels = (emotions) => {
    const levels = { happy: 0, sad: 0, angry: 0, anxious: 0, confused: 0 };
    const emotionCounts = {};

    // Count occurrences of each emotion
    emotions.forEach((emotion) => {
      if (emotionCounts[emotion]) {
        emotionCounts[emotion] += 1;
      } else {
        emotionCounts[emotion] = 1;
      }
    });

    // Calculate percentage levels for each emotion

    const totalSentences = emotions.length;
    levels.happy = (
      ((emotionCounts.happy || 0) / totalSentences) *
      100
    ).toFixed(2);
    levels.sad = (((emotionCounts.sad || 0) / totalSentences) * 100).toFixed(2);
    levels.angry = (
      ((emotionCounts.angry || 0) / totalSentences) *
      100
    ).toFixed(2);
    levels.anxious = (
      ((emotionCounts.anxious || 0) / totalSentences) *
      100
    ).toFixed(2);
    levels.confused = (
      ((emotionCounts.confused || 0) / totalSentences) *
      100
    ).toFixed(2);

    return levels;
  };

  // Handle Submit button click
  const handleSubmit = () => {
    setLoadingSubmit(true);
    axios
      .post("http://localhost:8080/predict-emotion", { paragraph: journal })
      .then((response) => {
        console.log("Predicted Emotion:", response.data);
        const levels = mapEmotionsToLevels(
          response.data.sentence_emotions.map((item) => item.emotion)
        );
        setEmotionLevels(levels);
        setLoadingSubmit(false);
      })
      .catch((error) => {
        console.error("Error analyzing emotion:", error);
        setLoadingSubmit(false);
      });
  };

  // Handle the Clear button click
  const handleClear = () => {
    setJournal("");
    setEmotionLevels({ happy: 0, sad: 0, angry: 0, anxious: 0, confused: 0 });
    setExerciseSuggestion("");
  };

  // Handle submit for exercise suggestion
  const handleExerciseSuggestion = () => {
    setLoadingExercise(true);
    axios
      .post("http://localhost:8080/suggest-exercise", { journal })
      .then((response) => {
        setExerciseSuggestion(response.data.exercise);
        setLoadingExercise(false);
      })
      .catch((error) => {
        console.error("Error fetching exercise suggestion:", error);
        setLoadingExercise(false);
      });
  };

  return (
    <div className="dashboard-container">
      {/* NavBar */}
      <NavBar />

      {/* Left Section - Journal Input */}
      <JournalInput
        journal={journal}
        handleJournalChange={handleJournalChange}
        handleSubmit={handleSubmit}
        handleClear={handleClear}
        loadingSubmit={loadingSubmit}
      />

      {/* Right Section - Emotional Tracking */}
      <div className="right-panel">
        <EmotionTrackBar emotionLevels={emotionLevels} />
        {/* <EmotionGraph /> */}
        <EmotionLineChart data={lineChartData} />
        {/* <EmotionWordCloud words={wordCloudData} /> */}
        <ExercisePanel exercise={exerciseSuggestion} />{" "}
        <button className="exercise-btn" onClick={handleExerciseSuggestion}>
          {loadingExercise ? "Loading..." : "Get Exercise Suggestions"}
        </button>
      </div>
    </div>
  );
};

export default Dashboard;
