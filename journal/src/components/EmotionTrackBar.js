import React from "react";
import { CircularProgressbar, buildStyles } from "react-circular-progressbar";
import "react-circular-progressbar/dist/styles.css";

const EmotionTrackBar = ({
  emotionLevels = { happy: 0, sad: 0, angry: 0, anxious: 0, confused: 0 },
}) => {
  return (
    <div className="emotion-track">
      <h3>Emotion Levels</h3>
      <div className="circular-bars">
        <div className="circular-bar">
          <span>Happiness</span>
          <CircularProgressbar
            value={emotionLevels.happy || 0}
            text={`${emotionLevels.happy || 0}%`}
            styles={buildStyles({
              pathColor: "#00e676", // Green for happy
              textColor: "#333",
              trailColor: "#d6d6d6",
            })}
          />
        </div>
        <div className="circular-bar">
          <span>Sadness</span>
          <CircularProgressbar
            value={emotionLevels.sad || 0}
            text={`${emotionLevels.sad || 0}%`}
            styles={buildStyles({
              // pathColor: "#ff3d00", // Red for sad
              pathColor: "#29b6f6", // blue for sad
              textColor: "#333",
              trailColor: "#d6d6d6",
            })}
          />
        </div>
        <div className="circular-bar">
          <span>Anger</span>
          <CircularProgressbar
            value={emotionLevels.angry || 0}
            text={`${emotionLevels.angry || 0}%`}
            styles={buildStyles({
              pathColor: "#ff1744", // Darker red for anger
              textColor: "#333",
              trailColor: "#d6d6d6",
            })}
          />
        </div>
        <div className="circular-bar">
          <span>Anxiety</span>
          <CircularProgressbar
            value={emotionLevels.anxious || 0}
            text={`${emotionLevels.anxious || 0}%`}
            styles={buildStyles({
              pathColor: "#cdde60", // Yellow for anxious
              textColor: "#333",
              trailColor: "#d6d6d6",
            })}
          />
        </div>
        <div className="circular-bar">
          <span>Confusion</span>
          <CircularProgressbar
            value={emotionLevels.confused || 0}
            text={`${emotionLevels.confused || 0}%`}
            styles={buildStyles({
              pathColor: "#9c27b0", // Blue for confused
              textColor: "#333",
              trailColor: "#d6d6d6",
            })}
          />
        </div>
      </div>
    </div>
  );
};

export default EmotionTrackBar;
