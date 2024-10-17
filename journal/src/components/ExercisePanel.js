import React from "react";

const ExercisePanel = ({ exercise }) => {
  return (
    <div className="exercise-panel">
      <h3>Exercise Suggestions</h3>
      {exercise ? (
        <div
          className="formatted-exercise"
          dangerouslySetInnerHTML={{ __html: exercise }}
        />
      ) : (
        <p>No exercises yet. Enter a journal to get suggestions.</p>
      )}
    </div>
  );
};

export default ExercisePanel;
