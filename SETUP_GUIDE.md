# Setup Guide - What to Do Next

## ✅ Files Organized

All project files have been organized into the `iot-analytics-project/` folder with the following structure:

```
iot-analytics-project/
├── .github/workflows/     # GitHub Actions workflow
├── src/                   # FastAPI application
├── data/                  # All data files
├── tests/                 # All test files
├── scripts/               # Utility scripts
├── docs/                  # Documentation
└── requirements.txt       # Dependencies
```

## 🎯 Step-by-Step Instructions

### Step 1: Navigate to Project Folder

```bash
cd iot-analytics-project
```

### Step 2: Verify Files Are in Place

Check that all files are copied correctly:

```bash
# Windows PowerShell
Get-ChildItem -Recurse -File | Select-Object FullName

# Or check specific directories
ls src/
ls data/
ls tests/
```

### Step 3: Update File Paths (if needed)

The `main.py` file has been updated to use relative paths. If you encounter issues, verify the path in `src/main.py`:

```python
# Should reference: ../data/q-fastapi-timeseries-cache.csv
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 5: Test the Application

```bash
# Start the server
python src/main.py

# In another terminal, test it
python tests/quick_test.py
```

### Step 6: Initialize Git Repository

```bash
# Initialize git (if not already done)
git init

# Create .gitignore
echo "__pycache__/" > .gitignore
echo "*.pyc" >> .gitignore
echo ".env" >> .gitignore
echo "venv/" >> .gitignore

# Add all files
git add .

# Commit
git commit -m "Initial commit: Organized IoT Analytics Project"
```

### Step 7: Create GitHub Repository

1. Go to [GitHub](https://github.com) and create a new repository
2. Name it (e.g., `iot-analytics-project`)
3. **Don't** initialize with README (you already have one)
4. Copy the repository URL

### Step 8: Push to GitHub

```bash
# Add remote
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### Step 9: Update Email Address

Edit `docs/README.md` and replace `your.email@example.com` with your actual email address.

### Step 10: Verify GitHub Actions

1. Go to your GitHub repository
2. Click on the "Actions" tab
3. You should see the "Multi-Platform Matrix Build" workflow
4. It will run automatically on push, or you can trigger it manually

## 🔍 Verification Checklist

- [ ] All files copied to `iot-analytics-project/`
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Server runs successfully (`python src/main.py`)
- [ ] Tests pass (`python tests/quick_test.py`)
- [ ] Git repository initialized
- [ ] Code pushed to GitHub
- [ ] Email address updated in README
- [ ] GitHub Actions workflow runs successfully

## 🐛 Troubleshooting

### Issue: "File not found" when running main.py

**Solution**: Make sure you're running from the project root:
```bash
cd iot-analytics-project
python src/main.py
```

### Issue: Import errors

**Solution**: Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: GitHub Actions not running

**Solution**: 
1. Check that `.github/workflows/matrix-build.yml` exists
2. Verify the workflow file syntax is correct
3. Push to `main` or `master` branch
4. Or trigger manually via "Actions" tab → "Run workflow"

## 📞 Need Help?

- Check `docs/` folder for detailed documentation
- Review `PROJECT_STRUCTURE.md` for file organization
- See `docs/README.md` for API documentation

## 🎉 You're All Set!

Once you complete these steps, you'll have:
- ✅ Organized project structure
- ✅ Working FastAPI application
- ✅ GitHub repository with CI/CD
- ✅ All tests and scripts in place

Good luck with your project! 🚀

