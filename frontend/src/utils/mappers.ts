const normalizeInput = (value: string): string => value.trim();

export const mapSensitivity = (value: string): string => {
  const normalized = normalizeInput(value);

  switch (normalized) {
    case "High":
    case "Medium":
      return "Yes";
    case "Low":
    default:
      return "No";
  }
};

export const mapConcern = (value: string): string => {
  const normalized = normalizeInput(value);

  switch (normalized) {
    case "Fine Lines":
      return "Wrinkles";
    case "Large Pores":
      return "Open Pores";
    case "Dark Spots":
      return "Dark Spots";
    case "Acne":
    case "Redness":
    case "Dullness":
      return normalized;
    default:
      return "Acne";
  }
};

export const mapSkinType = (value: string): string => {
  const normalized = normalizeInput(value);

  switch (normalized) {
    case "Oily":
    case "Dry":
    case "Normal":
    case "Combination":
      return normalized;
    default:
      return "Normal";
  }
};
